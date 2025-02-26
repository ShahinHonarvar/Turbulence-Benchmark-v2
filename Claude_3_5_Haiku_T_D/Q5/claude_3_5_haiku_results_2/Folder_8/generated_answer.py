def all_neg_ints_inclusive(nums):
    if len(nums) <= 23:
        return []
    target_value = nums[23]
    return [num for num in nums[23:24] if num < 0]