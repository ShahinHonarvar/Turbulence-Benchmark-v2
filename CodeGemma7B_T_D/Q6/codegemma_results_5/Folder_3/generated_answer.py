def all_neg_ints_exclusive(nums):
    negative_ints = []
    for i in range(78, 93):
        if nums[i] < 0:
            negative_ints.append(nums[i])
    return negative_ints