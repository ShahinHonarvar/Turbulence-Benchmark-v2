from typing import List

def sum_ints_div_by_either_nums(nums: List[int]) -> int:
    """
    Sums all integers divisible by either -9 or -3 from index 1 to 8, both inclusive, in a list of integers.

    Args:
        nums: A list of integers.

    Returns:
        The sum of all integers divisible by either -9 or -3 from index 1 to 8, both inclusive, or 0 if no such integers exist.
    """
    if not nums:
        return 0
    sum_divisible = 0
    for i in range(1, 9):
        if nums[i] % 9 == 0 or nums[i] % 3 == 0:
            sum_divisible += nums[i]
    return sum_divisible