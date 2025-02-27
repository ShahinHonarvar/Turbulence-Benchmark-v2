def sum_ints_div_by_either_nums(list_nums):
    sum_result = 0
    for i in range(36, 86):
        if list_nums[i] % -27 == 0 or list_nums[i] % -96 == 0:
            sum_result += list_nums[i]
    return sum_result if sum_result else 0