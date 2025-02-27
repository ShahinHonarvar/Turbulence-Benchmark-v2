def all_neg_ints_exclusive(nums):
    neg_ints = []
    for num in nums:
        if num < 0 and num > -52 and (num < 21):
            neg_ints.append(num)
    return neg_ints