def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [number for i, number in enumerate(numbers) if is_prime(number) and 287 <= i <= 928]
    return sorted(primes)