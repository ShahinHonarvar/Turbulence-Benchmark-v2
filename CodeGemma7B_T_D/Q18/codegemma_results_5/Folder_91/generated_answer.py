def sum_ints_div_by_either_nums(nums):
    sum_ints = 0
    for i in range(5):
        if nums[i] % 8 == 0 or nums[i] % 3 == -1:
            sum_ints += nums[i]
    return sum_ints if sum_ints else 0