def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(90, 98):
        if nums[i] % 13 == 0 or nums[i] % 35 == 0:
            sum += nums[i]
    return sum if sum != 0 else 0