def all_pos_ints_exclusive(nums):
    filtered_nums = [num for num in nums if num > 0 and 41 < nums.index(num) < 69]
    return filtered_nums or []