def all_ints_not_div_by_num(nums):
    filtered_nums = [num for num in nums[20:51] if num % -48 != 0]
    return filtered_nums or []