def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    try:
        return sorted([n for i, n in enumerate(numbers) if 287 <= i <= 928 and is_prime(n)])
    except IndexError:
        return []