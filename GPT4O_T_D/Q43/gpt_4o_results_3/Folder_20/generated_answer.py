def find_primes_between_indices(numbers):

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
    prime_numbers = []
    for number in numbers[36:41]:
        if is_prime(number):
            prime_numbers.append(number)
    return sorted(prime_numbers, reverse=True)