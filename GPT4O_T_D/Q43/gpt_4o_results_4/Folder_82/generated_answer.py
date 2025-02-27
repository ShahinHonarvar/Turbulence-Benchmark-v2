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
    if len(numbers) < 73:
        return []
    sub_list = numbers[25:73]
    primes = [num for num in sub_list if is_prime(num)]
    return sorted(primes)