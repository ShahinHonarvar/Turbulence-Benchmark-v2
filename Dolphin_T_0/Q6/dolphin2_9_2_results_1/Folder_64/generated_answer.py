def all_neg_ints_exclusive(nums):
    neg_nums = []
    for i in range(1, len(nums) - 1):
        if nums[i] < 0:
            neg_nums.append(nums[i])
    return neg_nums