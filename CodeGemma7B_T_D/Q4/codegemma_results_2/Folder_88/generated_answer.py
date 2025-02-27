def all_pos_ints_exclusive(nums):
    filtered_list = [num for num in nums if isinstance(num, int) and num > 0 and (2 < num < 9)]
    return filtered_list or []