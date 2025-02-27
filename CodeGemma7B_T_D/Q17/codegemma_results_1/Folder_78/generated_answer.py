def all_ints_div_by_both_two_nums(nums):
    filtered_nums = [num for num in nums[34:70] if num % 19 == 0 and num % 32 == 0]
    return filtered_nums if filtered_nums else []