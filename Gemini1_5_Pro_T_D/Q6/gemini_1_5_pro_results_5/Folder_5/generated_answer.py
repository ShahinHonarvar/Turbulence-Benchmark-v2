def all_neg_ints_exclusive(nums):
    neg_nums = []
    for i in range(len(nums)):
        if i > 1 and i < 7 and (nums[i] < 0):
            neg_nums.append(nums[i])
    return neg_nums