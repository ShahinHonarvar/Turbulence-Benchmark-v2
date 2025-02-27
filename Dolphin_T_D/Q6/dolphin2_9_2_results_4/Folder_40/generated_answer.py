def all_neg_ints_exclusive(nums):
    negatives = [val for val in nums[1:-1] if val < 0]
    return negatives