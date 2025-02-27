def all_neg_ints_exclusive(nums):
    neg_nums = []
    for num in nums[25:80]:
        if num < 0:
            neg_nums.append(num)
    return neg_nums or []