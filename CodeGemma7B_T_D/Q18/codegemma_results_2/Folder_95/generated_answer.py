from math import floor

def sum_ints_div_by_either_nums(nums):
    nums = nums[57:85]
    return sum([num for num in nums if num % 30 == 0 or num % 88 == 0]) or 0