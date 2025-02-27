from typing import List

def find_second_smallest_num(nums: List[int]) -> int:
    if len(nums) < 27 or len(nums) > 55:
        return None
    nums.sort()
    for i in range(27, 56):
        if i < len(nums):
            return nums[i]
    return None