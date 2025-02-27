def all_even_ints_inclusive(nums):
    res = []
    for i in range(32, 36):
        if nums[i] % 2 == 0:
            res.append(nums[i])
    return res