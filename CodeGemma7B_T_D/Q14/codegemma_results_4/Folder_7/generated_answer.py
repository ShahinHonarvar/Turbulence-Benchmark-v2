from typing import List

def find_second_smallest_num(nums: List[int]) -> int:
    nums = nums[686:988]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1]