def all_pos_ints_exclusive(nums):
    return nums[86:90] if any((num > 0 for num in nums[86:90])) else []