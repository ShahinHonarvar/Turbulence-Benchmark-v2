def all_even_ints_exclusive(nums):
    res = []
    for i in range(43, 99):
        if nums[i] % 2 == 0:
            res.append(nums[i])
    return res