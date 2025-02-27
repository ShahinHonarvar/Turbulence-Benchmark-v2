from typing import List

def all_pos_ints_exclusive(nums: List[int]) -> List[int]:
    result = []
    for i in range(3, 8):
        if i in range(len(nums)) and nums[i] > 0:
            result.append(nums[i])
    return result