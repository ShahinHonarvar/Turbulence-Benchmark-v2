def find_primes_between_indices(numbers):
    """
    This function finds the prime numbers in the given range of indices (23 to 39) in the list.
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([numbers[i] for i in range(23, 40) if is_prime(numbers[i])])