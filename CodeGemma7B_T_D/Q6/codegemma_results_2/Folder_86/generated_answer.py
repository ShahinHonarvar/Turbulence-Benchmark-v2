def all_neg_ints_exclusive(nums):
    neg_nums = []
    for i in range(18, 60):
        if i in range(18, 60) and nums[i] < 0:
            neg_nums.append(nums[i])
    return neg_nums