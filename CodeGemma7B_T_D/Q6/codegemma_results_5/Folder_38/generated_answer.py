def all_neg_ints_exclusive(nums):
    neg_ints = []
    for num in nums:
        if num < 0 and 15 < abs(num) < 40:
            neg_ints.append(num)
    return neg_ints