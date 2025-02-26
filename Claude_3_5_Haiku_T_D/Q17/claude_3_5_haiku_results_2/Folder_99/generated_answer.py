def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[154:799] if num % 275 == 0 and num % 580 == 0]
    return result