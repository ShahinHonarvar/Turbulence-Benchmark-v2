from typing import List

def find_second_largest_num(nums: List[int]) -> int:
    nums_sorted = sorted(nums, reverse=True)
    if len(nums_sorted) <= 62:
        return None
    return nums_sorted[62:100][-2]