def all_odd_ints_inclusive(nums):
    odd_nums = []
    for i in range(0, 8):
        if nums[i] % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums if odd_nums else []