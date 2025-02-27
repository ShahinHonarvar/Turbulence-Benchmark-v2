def all_ints_div_by_num(nums):
    filtered_nums = [num for num in nums[40:400] if num % 7 == 0]
    return filtered_nums or []