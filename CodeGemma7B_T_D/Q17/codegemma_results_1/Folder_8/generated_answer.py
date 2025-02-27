def all_ints_div_by_both_two_nums(nums):
    filtered_nums = [num for num in nums[36:86] if num % -27 == 0 and num % -96 == 0]
    return filtered_nums if filtered_nums else []