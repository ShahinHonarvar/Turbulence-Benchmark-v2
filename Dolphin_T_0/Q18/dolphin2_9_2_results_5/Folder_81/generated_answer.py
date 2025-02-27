def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(10, 101):
        if nums[i] % 10 == 0 or nums[i] % 100 == 0:
            sum += nums[i]
    return sum if sum != 0 else 0