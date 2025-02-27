def all_neg_ints_exclusive(nums):
    neg_nums = []
    for i in range(51, 92):
        if i < len(nums) and nums[i] < 0:
            neg_nums.append(nums[i])
    return neg_nums