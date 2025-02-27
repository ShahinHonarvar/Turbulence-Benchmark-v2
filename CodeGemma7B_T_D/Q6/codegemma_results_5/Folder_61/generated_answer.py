def all_neg_ints_exclusive(nums):
    return [num for num in nums if num in range(-7, 0, 1) and num not in nums[8:]]