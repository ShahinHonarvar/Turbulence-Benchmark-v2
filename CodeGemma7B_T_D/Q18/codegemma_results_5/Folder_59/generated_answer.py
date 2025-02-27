def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i in range(0, 9):
        if nums[i] in [-3, 8]:
            sum_of_ints += nums[i]
    return sum_of_ints