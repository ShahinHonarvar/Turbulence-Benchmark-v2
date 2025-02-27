def all_neg_ints_exclusive(nums):
    negatives = []
    for i in range(87, 96):
        if nums[i] < 0:
            negatives.append(nums[i])
    return negatives