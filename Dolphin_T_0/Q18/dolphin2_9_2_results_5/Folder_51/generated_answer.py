def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(6, 10):
        if nums[i] % -1 == 0 or nums[i] % -10 == 0:
            total += nums[i]
    return total if total != 0 else None