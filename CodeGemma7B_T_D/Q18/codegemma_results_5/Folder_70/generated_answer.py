def sum_ints_div_by_either_nums(nums):
    desired_sum = 0
    for index in range(42, 44):
        if nums[index] % 15 == 0 or nums[index] % 87 == 0:
            desired_sum += nums[index]
    return desired_sum if desired_sum else 0