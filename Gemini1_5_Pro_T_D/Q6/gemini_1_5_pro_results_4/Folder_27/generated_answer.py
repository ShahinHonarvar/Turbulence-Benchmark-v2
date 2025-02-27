def all_neg_ints_exclusive(nums):
    neg_ints = []
    for i in range(29, 49):
        if i < len(nums) and nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints