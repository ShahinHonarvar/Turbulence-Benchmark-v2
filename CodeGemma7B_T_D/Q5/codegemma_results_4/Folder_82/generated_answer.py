def all_neg_ints_inclusive(nums):
    neg_nums = []
    for num in nums[20:201]:
        if num <= 0:
            neg_nums.append(num)
    return neg_nums