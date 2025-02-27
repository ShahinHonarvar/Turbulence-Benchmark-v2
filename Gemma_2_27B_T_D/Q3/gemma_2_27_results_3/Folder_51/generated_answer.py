def all_pos_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 1 and i <= 8 and (num > 0)]