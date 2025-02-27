def all_ints_not_div_by_num(nums):
    filtered_nums = [num for num in nums[64:80] if num % -95 != 0]
    return filtered_nums or []