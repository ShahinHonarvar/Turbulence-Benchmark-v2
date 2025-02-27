def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(77, 88):
        if nums[i] % 23 == 0 or nums[i] % 57 == 0:
            sum += nums[i]
    return sum if sum else 0