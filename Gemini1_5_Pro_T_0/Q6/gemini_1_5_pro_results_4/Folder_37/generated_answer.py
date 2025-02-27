def all_neg_ints_exclusive(nums):
    result = []
    for i in range(len(nums)):
        if i > 0 and i < len(nums) - 1 and (nums[i] < 0):
            result.append(nums[i])
    return result