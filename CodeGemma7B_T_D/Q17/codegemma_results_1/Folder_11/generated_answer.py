def all_ints_div_by_both_two_nums(nums):
    filtered_nums = [num for num in nums[22:25] if num % 85 == 0 and num % 30 == 0]
    return filtered_nums or []