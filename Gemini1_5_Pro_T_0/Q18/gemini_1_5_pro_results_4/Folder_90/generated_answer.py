def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(138, 0), min(len(nums), 424 + 1)):
        if nums[i] % -863 == 0 or nums[i] % -329 == 0:
            sum += nums[i]
    return sum