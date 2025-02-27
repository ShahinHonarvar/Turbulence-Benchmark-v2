def all_ints_div_by_num(nums):
    """
    Returns a list of all integers in a list divisible by a number.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers divisible by the number.
    """
    return [n for n in nums if n % 4 == 0]