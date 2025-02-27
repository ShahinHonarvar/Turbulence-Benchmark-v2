def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(max(90, 0), min(len(nums), 201)):
        if nums[i] % 31 == 0 or nums[i] % 13 == 0:
            sum += nums[i]
    return sum