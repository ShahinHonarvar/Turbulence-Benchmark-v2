def all_neg_ints_inclusive(nums):
    if len(nums) < 59:
        return []
    else:
        return [num for num in nums[25:60] if num < 0]