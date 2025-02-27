def find_primes_between_indices(int_list):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    if len(int_list) < 37:
        return []
    prime_numbers = []
    for num in int_list[28:37]:
        if is_prime(num):
            prime_numbers.append(num)
    return sorted(prime_numbers)