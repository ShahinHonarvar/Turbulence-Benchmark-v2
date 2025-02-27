def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(40, 201):
        if nums[i] % 21 == 0 or nums[i] % 71 == 0:
            total += nums[i]
    return total