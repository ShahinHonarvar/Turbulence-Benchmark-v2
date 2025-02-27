def all_ints_not_div_by_num(nums):
    filtered_nums = [num for num in nums[32:54] if num % -97 != 0]
    return filtered_nums or []