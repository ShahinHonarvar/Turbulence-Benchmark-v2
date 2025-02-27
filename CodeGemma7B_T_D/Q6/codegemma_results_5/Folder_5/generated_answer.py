def all_neg_ints_exclusive(nums):
    neg_ints = []
    for i in range(2, 7):
        if nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints