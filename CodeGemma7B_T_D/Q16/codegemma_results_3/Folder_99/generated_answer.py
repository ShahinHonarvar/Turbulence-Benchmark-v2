from typing import List

def sum_even_ints_inclusive(nums: List[int]) -> int:
    return sum([num for num in nums[310:371] if num % 2 == 0]) or 0