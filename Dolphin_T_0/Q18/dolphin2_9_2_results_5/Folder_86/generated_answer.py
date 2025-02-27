def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(54, 80):
        if nums[i] % 54 == 0 or nums[i] % 28 == 0:
            total += nums[i]
    if total == 0:
        return 0
    else:
        return total