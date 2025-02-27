def all_neg_ints_exclusive(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] < 0 and i in range(0, 10):
            result.append(nums[i])
    return result