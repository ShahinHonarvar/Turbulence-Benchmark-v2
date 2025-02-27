def all_neg_ints_exclusive(nums):
    negative_nums = []
    for i in range(20, 200):
        if nums[i] < 0:
            negative_nums.append(nums[i])
    return negative_nums