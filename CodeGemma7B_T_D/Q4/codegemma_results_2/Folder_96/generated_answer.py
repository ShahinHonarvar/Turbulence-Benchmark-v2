def all_pos_ints_exclusive(nums):
    return [num for num in nums if num > 0 and num > 50 and (num < 200)] or []