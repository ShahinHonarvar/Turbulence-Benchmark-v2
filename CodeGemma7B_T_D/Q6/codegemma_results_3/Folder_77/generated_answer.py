def all_neg_ints_exclusive(nums):
    result = []
    for num in nums[111:473]:
        if num < 0:
            result.append(num)
    return result