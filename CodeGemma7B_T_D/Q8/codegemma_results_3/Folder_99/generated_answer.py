from typing import List

def all_even_ints_exclusive(nums: List[int]) -> List[int]:
    even_nums = []
    for i in range(295, 573):
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums