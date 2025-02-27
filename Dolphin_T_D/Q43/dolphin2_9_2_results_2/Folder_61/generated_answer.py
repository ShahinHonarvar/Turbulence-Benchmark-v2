def find_primes_between_indices(nums):
    """
    Function to get prime numbers in the list between given indices.
    """

    def is_prime(num):
        """
        Nested function to check if number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [num for num in nums[3:9] if is_prime(num)]
    return sorted(primes) if primes else []