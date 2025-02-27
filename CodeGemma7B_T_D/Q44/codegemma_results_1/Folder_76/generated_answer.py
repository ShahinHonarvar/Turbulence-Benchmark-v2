def composite_nums_between_indices(nums):
    """
    Returns a set of composite numbers in the given list between index 639 to index 975, inclusive.

    Args:
        nums: A list of positive integers.

    Returns:
        A set of composite numbers in the given list between index 639 to index 975, inclusive. An empty set if no composite number exists in the specified range.
    """
    composite_nums = set()
    for i in range(639, 976):
        if 640 <= i < len(nums) and (not is_prime(nums[i])):
            composite_nums.add(nums[i])
    return composite_nums

def is_prime(num):
    """
    Checks if the given number is prime.

    Args:
        num: The number to check.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True