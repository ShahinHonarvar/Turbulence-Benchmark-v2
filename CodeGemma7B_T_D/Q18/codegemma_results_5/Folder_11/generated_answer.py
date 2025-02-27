def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(22, 25):
        if nums[i] % 85 == 0 or nums[i] % 30 == 0:
            sum += nums[i]
    return sum if sum != 0 else 0