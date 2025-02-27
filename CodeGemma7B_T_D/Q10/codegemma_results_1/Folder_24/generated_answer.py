def all_odd_ints_exclusive(nums):
    odd_nums = []
    for i in range(13, 66):
        if i % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums if odd_nums else []