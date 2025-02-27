def all_neg_ints_inclusive(nums):
    neg_ints = []
    for index in range(4):
        if nums[index] < 0:
            neg_ints.append(nums[index])
    return neg_ints