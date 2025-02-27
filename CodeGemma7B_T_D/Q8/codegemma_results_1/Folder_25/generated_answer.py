from typing import List

def all_even_ints_exclusive(nums: List[int]) -> List[int]:
    return [num for num in nums if num % 2 == 0 and 41 < num != 69]