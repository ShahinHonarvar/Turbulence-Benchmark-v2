def find_primes_between_indices(numbers):
    if len(numbers) < 98:
        return []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [n for n in numbers[21:98] if is_prime(n)]
    return sorted(primes)