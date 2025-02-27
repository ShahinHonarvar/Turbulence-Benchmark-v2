def all_pos_ints_inclusive(nums):
    return [num for num in nums if num <= 3 and num >= 1] if any((num <= 3 and num >= 1 for num in nums)) else []