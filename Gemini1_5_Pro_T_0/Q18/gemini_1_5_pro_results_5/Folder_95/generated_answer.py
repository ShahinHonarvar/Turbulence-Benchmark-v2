def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(57, 0), min(len(nums), 85)):
        if nums[i] % -30 == 0 or nums[i] % -88 == 0:
            sum += nums[i]
    return sum