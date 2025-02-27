def all_pos_ints_inclusive(nums):
    return nums[29:79] if any((1 <= num <= 79 for num in nums)) else []