def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(min(7, len(nums))):
        if nums[i] % -5 == 0 or nums[i] % -6 == 0:
            total += nums[i]
    return total