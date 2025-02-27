def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(14, 0), min(len(nums), 94)):
        if nums[i] % 71 == 0 or nums[i] % 81 == 0:
            sum += nums[i]
    return sum