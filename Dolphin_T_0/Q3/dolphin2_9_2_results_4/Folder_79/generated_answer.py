def all_pos_ints_inclusive(nums):
    result = [num for i, num in enumerate(nums) if i in range(4, 5) and num > 0]
    return result