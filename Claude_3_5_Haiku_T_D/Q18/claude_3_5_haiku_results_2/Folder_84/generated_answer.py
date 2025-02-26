def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(78, 82):
        if i < len(nums):
            if nums[i] % 76 == 0 or nums[i] % 60 == 0:
                total += nums[i]
    return total