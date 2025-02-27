def all_pos_ints_inclusive(nums):
    res = []
    for i in range(22, 64):
        if i < len(nums) and nums[i] > 0:
            res.append(nums[i])
    return res if res else []