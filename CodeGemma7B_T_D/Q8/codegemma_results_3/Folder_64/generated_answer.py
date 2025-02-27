def all_even_ints_exclusive(nums):
    res = []
    for i in range(len(nums)):
        if i < 4 and nums[i] % 2 == 0:
            res.append(nums[i])
    return res