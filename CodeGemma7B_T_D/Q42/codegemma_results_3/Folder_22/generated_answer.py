def prime_factors(nums):
    """
            This function takes a list of positive integers as input and returns the set of all prime factors of the integer at index 72.

            Args:
                nums: A list of positive integers.

            Returns:
                The set of all prime factors of the integer at index 72.
            """
    prime_factors = set()
    num = nums[72]
    for factor in range(2, num + 1):
        while num % factor == 0:
            prime_factors.add(factor)
            num //= factor
    return prime_factors