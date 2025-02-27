def all_even_ints_inclusive(nums):
    res = []
    for i in range(667, 775):
        if i < len(nums) and nums[i] % 2 == 0:
            res.append(nums[i])
    return res