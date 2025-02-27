def all_neg_ints_inclusive(nums):
    result = []
    for i in range(11):
        if i >= 0 and i <= 10 and (nums[i] < 0):
            result.append(nums[i])
    return result