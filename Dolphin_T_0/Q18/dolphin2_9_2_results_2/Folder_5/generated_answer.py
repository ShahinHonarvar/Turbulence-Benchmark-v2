def sum_ints_div_by_either_nums(nums):
    total = 0
    if len(nums) >= 2:
        for i in range(2):
            if nums[i] % -6 == 0 or nums[i] % 4 == 0:
                total += nums[i]
    return total