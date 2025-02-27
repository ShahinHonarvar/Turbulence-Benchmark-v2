from typing import List

def all_ints_div_by_both_two_nums(nums: List[int]) -> List[int]:
    """
    Returns a list of all integers divisible by both 74 and 15 from index 25 to index 70, both inclusive.

    Args:
        nums: A list of integers.

    Returns:
        A list of all integers divisible by both 74 and 15 from index 25 to index 70, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for i in range(25, 71):
        if nums[i] % 74 == 0 and nums[i] % 15 == 0:
            result.append(nums[i])
    return result