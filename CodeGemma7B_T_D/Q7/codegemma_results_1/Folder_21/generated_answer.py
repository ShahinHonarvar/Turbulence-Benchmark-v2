from typing import List

def all_even_ints_inclusive(nums: List[int]) -> List[int]:
    return [num for num in nums[639:976] if num % 2 == 0] or []