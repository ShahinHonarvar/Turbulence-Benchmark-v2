from typing import Optional

def find_second_smallest_num(nums: list[int]) -> Optional[int]:
    nums.sort()
    if len(nums) > 8:
        return nums[9]
    else:
        return None