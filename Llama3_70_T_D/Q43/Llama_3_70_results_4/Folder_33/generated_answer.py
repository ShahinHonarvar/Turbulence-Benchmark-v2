def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = sorted([num for i, num in enumerate(numbers) if 289 <= i <= 381 and is_prime(num)], reverse=True)
    return primes