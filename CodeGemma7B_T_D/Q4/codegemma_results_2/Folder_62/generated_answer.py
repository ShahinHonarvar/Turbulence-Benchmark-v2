from typing import List

def all_pos_ints_exclusive(nums: List[int]) -> List[int]:
    """Return the list of all positive integers from index 55 to index 84, both exclusive."""
    return [n for n in nums[55:84] if n > 0]