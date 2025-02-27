def all_ints_div_by_both_two_nums(nums):
    filtered_nums = [num for num in nums[55:81] if num % 22 == 0 and num % 32 == 0]
    return filtered_nums if filtered_nums else []