def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(154, 799):
        if i >= len(nums):
            break
        if nums[i] % 275 == 0 or nums[i] % 580 == 0:
            total += nums[i]
    return total