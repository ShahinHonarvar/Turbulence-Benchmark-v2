def all_neg_ints_exclusive(nums):
    res = []
    for num in nums:
        if num < 0 and nums.index(num) >= 56 and (nums.index(num) < 92):
            res.append(num)
    return res