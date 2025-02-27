def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(32, 100):
        if nums[i % 11] + nums[i % 15] in [-22, -30]:
            sum += nums[i]
    return 0 if not sum else sum