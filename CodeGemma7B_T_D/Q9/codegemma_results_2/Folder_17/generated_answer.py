from typing import List

def all_odd_ints_inclusive(nums: List[int]) -> List[int]:
    """
    Returns a list of odd integers from index 62 to index 78, inclusive.
    """
    result = []
    for i in range(62, 79):
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result