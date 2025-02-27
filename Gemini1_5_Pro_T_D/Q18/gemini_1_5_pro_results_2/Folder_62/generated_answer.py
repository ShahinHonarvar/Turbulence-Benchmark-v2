def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(44, 60):
        if i >= len(nums):
            break
        if nums[i] % 39 == 0 or nums[i] % 15 == 0:
            sum += nums[i]
    return sum