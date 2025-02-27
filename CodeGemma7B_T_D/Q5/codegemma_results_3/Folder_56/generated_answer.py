def all_neg_ints_inclusive(nums):
    neg_nums = []
    for num in nums:
        if num >= -1:
            continue
        neg_nums.append(num)
    return neg_nums