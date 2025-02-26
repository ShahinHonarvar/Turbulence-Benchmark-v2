def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(73, 87):
        if i < len(nums):
            if nums[i] % 54 == 0 or nums[i] % 82 == 0:
                total += nums[i]
    return total