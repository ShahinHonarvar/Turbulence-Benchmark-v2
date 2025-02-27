def all_pos_ints_exclusive(nums):
    res = []
    lo, hi = (32, 99)
    for num in nums:
        if num > 0 and lo <= num < hi:
            res.append(num)
    return res