def all_odd_ints_exclusive(nums):
    res = []
    for i in range(73, 84):
        if nums[i] % 2 == 1:
            res.append(nums[i])
    return res if len(res) > 0 else []