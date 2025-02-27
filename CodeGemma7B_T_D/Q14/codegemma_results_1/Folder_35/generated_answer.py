from typing import List

def find_second_smallest_num(nums: List[int]) -> int | None:
    nums = nums[15:39 + 1]
    nums.sort()
    return nums[1] if len(nums) >= 2 else None