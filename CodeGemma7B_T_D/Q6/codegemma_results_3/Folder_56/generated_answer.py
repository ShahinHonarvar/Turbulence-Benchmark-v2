def all_neg_ints_exclusive(nums):
    neg_ints = []
    for i in range(7, 9):
        if nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints