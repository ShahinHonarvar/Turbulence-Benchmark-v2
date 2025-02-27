def all_neg_ints_inclusive(nums):
    if len(nums) < 43:
        return []
    else:
        return [num for num in nums[43:52] if num < 0]