def all_pos_ints_inclusive(nums):
    return nums[6:7 + 1] if any((num >= 0 for num in nums[6:7 + 1])) else []