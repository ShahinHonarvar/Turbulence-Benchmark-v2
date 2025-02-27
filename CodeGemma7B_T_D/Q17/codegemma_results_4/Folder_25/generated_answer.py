from typing import List

def all_ints_div_by_both_two_nums(nums: List[int]) -> List[int]:
    return [num for num in nums[25:81] if num % 20 == 0 and num % 26 == 0]