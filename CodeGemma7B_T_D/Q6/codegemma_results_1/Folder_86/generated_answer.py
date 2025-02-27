def all_neg_ints_exclusive(nums):
    result = []
    for i in range(18, 60):
        if nums[i] < 0:
            result.append(nums[i])
    return result