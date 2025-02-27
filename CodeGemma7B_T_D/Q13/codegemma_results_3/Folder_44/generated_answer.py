from typing import Any

def find_second_largest_num(nums: list[int]) -> Any:
    nums = sorted(nums[13:69])
    if len(nums) < 2:
        return None
    return nums[-2]