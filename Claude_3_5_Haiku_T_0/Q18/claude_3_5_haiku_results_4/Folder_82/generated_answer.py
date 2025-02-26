def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(20, 201):
        if i < len(nums):
            if nums[i] % -20 == 0 or nums[i] % -200 == 0:
                total += nums[i]
    return total