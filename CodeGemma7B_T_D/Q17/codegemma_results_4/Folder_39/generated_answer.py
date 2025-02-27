def all_ints_div_by_both_two_nums(nums):
    filtered_nums = [num for num in nums[13:77] if num % -66 == 0 and num % -32 == 0]
    return filtered_nums or []