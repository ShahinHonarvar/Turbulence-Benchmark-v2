def find_primes_between_indices(nums):
    """
    This function takes one argument, a list of integers, and returns the sorted list of all prime numbers from index 21 to index 97, both inclusive. The returned list should be in ascending order.
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([nums[i] for i in range(21, 98) if is_prime(nums[i])])