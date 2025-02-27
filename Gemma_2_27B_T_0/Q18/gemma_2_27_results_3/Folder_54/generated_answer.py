def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(13, 92):
        if nums[i] % -65 == 0 or nums[i] % -62 == 0:
            total += nums[i]
    return total