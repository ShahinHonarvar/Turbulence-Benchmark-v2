from typing import Optional

def find_second_largest_num(nums: list[int]) -> Optional[int]:
    pos_num = sorted(nums[27:56])
    return pos_num[len(pos_num) - 2] if len(pos_num) >= 2 else None