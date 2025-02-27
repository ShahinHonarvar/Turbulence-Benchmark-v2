def all_pos_ints_exclusive(nums):
    res = []
    for num in nums[1:8]:
        if num > 0:
            res.append(num)
    return res