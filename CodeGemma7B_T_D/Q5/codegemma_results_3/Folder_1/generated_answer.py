def all_neg_ints_inclusive(nums):
    result = []
    for i in range(31, 72):
        if nums[i] < 0:
            result.append(nums[i])
    return result if result else []