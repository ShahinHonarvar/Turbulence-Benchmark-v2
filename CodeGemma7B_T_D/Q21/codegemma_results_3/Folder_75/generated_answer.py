from functools import cmp_to_key

def all_ints_div_by_num(nums):
    filtered_nums = [num for num in nums[12:34] if num % -91 == 0]
    return filtered_nums or []