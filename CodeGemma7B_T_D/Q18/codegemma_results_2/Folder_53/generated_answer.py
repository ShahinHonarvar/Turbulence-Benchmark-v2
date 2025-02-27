def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(200, 201):
        if nums[i % len(nums)] % (17 or -5) == 0:
            sum += nums[i % len(nums)]
    if sum == 0:
        return 0
    else:
        return sum