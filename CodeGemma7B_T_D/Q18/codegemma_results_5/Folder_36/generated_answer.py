def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(299, 383):
        if nums[i] % 858 == 0 or nums[i] % 952 == 0:
            sum += nums[i]
    if sum == 0:
        return 0
    return sum