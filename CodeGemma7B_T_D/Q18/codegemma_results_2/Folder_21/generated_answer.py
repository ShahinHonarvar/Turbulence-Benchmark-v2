def sum_ints_div_by_either_nums(nums):
    sum_value = 0
    for i in range(315, 935):
        if nums[i] % -897 == 0 or nums[i] % -556 == 0:
            sum_value += nums[i]
    return sum_value