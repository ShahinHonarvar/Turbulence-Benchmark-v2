def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(len(nums)):
        if i >= 58 and i <= 81:
            if nums[i] % 55 == 0 or nums[i] % 10 == 0:
                sum += nums[i]
    return sum