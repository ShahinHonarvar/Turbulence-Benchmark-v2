def all_pos_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i in range(6) and num > 0]