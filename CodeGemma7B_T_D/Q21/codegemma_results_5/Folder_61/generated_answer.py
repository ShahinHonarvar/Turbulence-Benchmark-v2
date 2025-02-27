from typing import List

def all_ints_div_by_num(nums: List[int]) -> List[int]:
    return [num for num in nums if num % 7 == 0 and num in range(0, len(nums))]