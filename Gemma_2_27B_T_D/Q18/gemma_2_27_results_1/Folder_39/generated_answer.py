def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(13, 77):
        if nums[i] % -66 == 0 or nums[i] % -32 == 0:
            total += nums[i]
    return total