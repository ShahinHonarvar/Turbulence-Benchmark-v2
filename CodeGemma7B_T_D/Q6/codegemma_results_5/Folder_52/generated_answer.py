def all_neg_ints_exclusive(nums):
    negative_nums = []
    for i in range(93, 94):
        if nums[i] < 0:
            negative_nums.append(nums[i])
    return negative_nums