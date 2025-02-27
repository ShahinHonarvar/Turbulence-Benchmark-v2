def sum_ints_div_by_either_nums(nums):
    sum_result = 0
    for i in range(55, 81):
        if nums[i] % 22 == 0 or nums[i] % 32 == 0:
            sum_result += nums[i]
    return sum_result if sum_result != 0 else 0