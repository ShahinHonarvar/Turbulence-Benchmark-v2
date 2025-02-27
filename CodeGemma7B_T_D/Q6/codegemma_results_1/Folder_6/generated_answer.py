def all_neg_ints_exclusive(nums):
    neg_nums = []
    for num in nums[86:99]:
        if num < 0:
            neg_nums.append(num)
    if not neg_nums:
        return []
    return neg_nums