def all_pos_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if num > 0 and 100 <= i <= 200]