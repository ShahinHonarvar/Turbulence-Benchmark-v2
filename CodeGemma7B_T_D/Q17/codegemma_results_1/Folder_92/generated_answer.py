from sympy import Divisible

def all_ints_div_by_both_two_nums(nums):
    divisible_by_both_two_nums = [num for num in nums if num % 1 == 0 and num % -1 == 0 and (num >= nums[0]) and (num <= nums[len(nums) - 1])]
    return divisible_by_both_two_nums