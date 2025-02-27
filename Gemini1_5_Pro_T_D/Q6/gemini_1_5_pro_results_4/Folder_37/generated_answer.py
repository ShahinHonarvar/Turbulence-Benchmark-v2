def all_neg_ints_exclusive(nums):
    neg_nums = []
    for i in range(len(nums)):
        if i > 0 and i < len(nums) - 1 and (nums[i] < 0):
            neg_nums.append(nums[i])
    return neg_nums