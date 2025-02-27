def all_neg_ints_exclusive(nums):
    neg_ints = []
    for i in range(len(nums)):
        if nums[i] < 0 and (i == 0 or nums[i - 1] >= 0):
            neg_ints.append(nums[i])
    return neg_ints