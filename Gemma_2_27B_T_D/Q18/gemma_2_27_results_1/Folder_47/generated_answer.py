def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(42, 88):
        if nums[i] % -90 == 0 or nums[i] % -74 == 0:
            total += nums[i]
    return total