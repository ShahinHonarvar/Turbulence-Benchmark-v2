from typing import List

def all_neg_ints_exclusive(nums: List[int]) -> List[int]:
    """Extract all negative integers from index 4 to index 5, both exclusive."""
    return [num for num in nums[4:5] if num < 0]