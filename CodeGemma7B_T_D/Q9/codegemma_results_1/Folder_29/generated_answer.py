def all_odd_ints_inclusive(nums):
    res = []
    for i in range(59, 98):
        if i % 2 != 0:
            res.append(nums[i])
    return res if res else []