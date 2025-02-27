def find_primes_between_indices(lst):
    """Function to find prime numbers in a given list within a specific range of indices."""

    def is_prime(n):
        """Function to check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [lst[i] for i in range(10, 67) if is_prime(lst[i])]
    return sorted(primes)