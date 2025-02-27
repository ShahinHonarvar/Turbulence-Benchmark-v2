def sum_ints_div_by_either_nums(nums):
    total = 0
    for k in range(57, 86):
        if nums[k] % -77 == 0 or nums[k] % -32 == 0:
            total += nums[k]
    return total if total else 0