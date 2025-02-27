def all_neg_ints_inclusive(nums):
    if len(nums) < 24:
        return []
    return [num for num in nums[23:24] if num < 0]