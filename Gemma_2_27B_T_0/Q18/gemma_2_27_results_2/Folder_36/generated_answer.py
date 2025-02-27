def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(299, 383):
        if nums[i] % 858 == 0 or nums[i] % 952 == 0:
            total += nums[i]
    return total