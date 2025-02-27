from typing import List

def sum_odd_ints_inclusive(nums: List[int]) -> int:
    return sum((num for num in nums[12:92 + 1] if num % 2))