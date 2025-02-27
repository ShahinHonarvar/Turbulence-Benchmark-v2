def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(58, 76):
        if i >= len(nums):
            break
        if nums[i] % 72 == 0 or nums[i] % 62 == 0:
            sum += nums[i]
    return sum