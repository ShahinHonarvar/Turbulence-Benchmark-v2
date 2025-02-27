def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(54, 80):
        if nums[i] % 54 == 0 or nums[i] % 28 == 0:
            sum += nums[i]
    return sum