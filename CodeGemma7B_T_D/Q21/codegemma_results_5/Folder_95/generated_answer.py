def all_ints_div_by_num(nums):
    filtered_nums = [num for num in nums[75:86] if num % 40 == 0]
    return filtered_nums or []