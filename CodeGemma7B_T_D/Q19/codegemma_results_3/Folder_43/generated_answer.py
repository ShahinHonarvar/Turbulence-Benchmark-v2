from typing import List

def all_ints_not_div_by_num(nums: List[int]) -> List[int]:
    """
    Returns the list of all integers not divisible by -15 from index 16 to index 87, both exclusive.
    If no such integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums[16:87] if num % -15 != 0]