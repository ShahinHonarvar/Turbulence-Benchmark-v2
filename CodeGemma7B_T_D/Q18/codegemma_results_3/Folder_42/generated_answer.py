def sum_ints_div_by_either_nums(nums):
    sum = 0
    for x in range(29, 46):
        if nums[x] % 27 == 0 or nums[x] % 81 == 0:
            sum += nums[x]
    return sum if sum else 0