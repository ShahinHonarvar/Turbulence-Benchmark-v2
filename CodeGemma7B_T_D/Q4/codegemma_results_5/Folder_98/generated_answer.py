from typing import List

def all_pos_ints_exclusive(nums: List[int]) -> List[int]:
    res = []
    for i in range(7):
        if nums[i] > 0 and i <= 6:
            res.append(i)
    return res