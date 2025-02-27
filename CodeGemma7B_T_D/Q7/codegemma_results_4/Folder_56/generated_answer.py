from typing import List

def all_even_ints_inclusive(nums: List[int]) -> List[int]:
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums