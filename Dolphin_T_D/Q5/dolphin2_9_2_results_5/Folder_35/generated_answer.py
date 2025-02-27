def all_neg_ints_inclusive(nums):
    neg_nums = []
    for i in range(30, 49):
        if nums[i] < 0:
            neg_nums.append(nums[i])
    return neg_nums