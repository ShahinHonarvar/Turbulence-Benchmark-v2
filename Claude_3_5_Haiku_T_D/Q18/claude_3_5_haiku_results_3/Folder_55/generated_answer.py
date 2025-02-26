def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(min(10, len(nums))):
        if nums[i] % 10 == 0 or nums[i] % 100 == 0:
            total += nums[i]
    return total