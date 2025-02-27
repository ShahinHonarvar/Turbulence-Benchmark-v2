def all_pos_ints_exclusive(nums):
    return [num for num in nums if num > 0 and num < 8 and (num not in range(1, 8))]