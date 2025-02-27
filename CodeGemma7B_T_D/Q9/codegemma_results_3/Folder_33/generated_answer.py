def all_odd_ints_inclusive(nums):
    res = []
    for i in range(667, 775):
        if nums[i] % 2 != 0:
            res.append(nums[i])
    return res