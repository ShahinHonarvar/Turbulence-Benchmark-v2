def all_ints_not_div_by_num(nums):
    filtered_nums = [num for num in nums[472:827] if num % 602 != 0]
    return filtered_nums or []