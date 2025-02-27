def all_pos_ints_exclusive(nums):
    result = [num for i, num in enumerate(nums) if 6 < i < 9 if num > 0]
    return result