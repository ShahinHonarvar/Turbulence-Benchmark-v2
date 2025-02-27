def all_neg_ints_inclusive(nums):
    neg_ints = []
    for i in range(1, 6):
        if i < len(nums) and nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints