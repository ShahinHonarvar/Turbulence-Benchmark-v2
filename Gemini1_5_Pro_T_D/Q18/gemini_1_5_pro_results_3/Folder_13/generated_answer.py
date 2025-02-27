def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(0, 13), min(len(nums), 19)):
        if nums[i] % 45 == 0 or nums[i] % 20 == 0:
            sum += nums[i]
    return sum