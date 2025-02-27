def all_neg_ints_inclusive(nums):
    neg_nums = []
    for i in range(len(nums)):
        if nums[i] < 0 and i <= 5:
            neg_nums.append(nums[i])
    return neg_nums