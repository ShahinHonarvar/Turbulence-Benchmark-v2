def find_primes_between_indices(numbers):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [number for number in numbers[17:80] if is_prime(number)]
    return sorted(primes, reverse=True) if primes else []