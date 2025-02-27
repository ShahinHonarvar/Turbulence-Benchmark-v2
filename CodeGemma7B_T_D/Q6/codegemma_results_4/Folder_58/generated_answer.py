def all_neg_ints_exclusive(nums):
    filtered = [num for num in nums[276:376] if num < 0]
    return filtered or []