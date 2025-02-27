def prime_factors(nums):
    """
    Finds the prime factors of the integer at index 100 in a list of positive integers.

    Args:
    nums: A list of positive integers.

    Returns:
    A set of all prime factors of the integer at index 100.
    """
    num = nums[100]
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors