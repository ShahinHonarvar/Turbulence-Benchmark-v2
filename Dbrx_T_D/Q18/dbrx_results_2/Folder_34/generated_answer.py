def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(len(nums)):
        if i >= 60 and i <= 200:
            if nums[i] % 9 == 0 or nums[i] % 11 == 0:
                total += nums[i]
    return total