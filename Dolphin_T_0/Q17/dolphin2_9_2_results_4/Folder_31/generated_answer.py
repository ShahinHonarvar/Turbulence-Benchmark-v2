def all_ints_div_by_both_two_nums(nums):
    target_nums = nums[56:89]
    result = [num for num in target_nums if num % -59 == 0 and num % -79 == 0]
    return result