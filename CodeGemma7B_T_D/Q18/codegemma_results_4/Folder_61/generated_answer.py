def sum_ints_div_by_either_nums(list_of_nums):
    result = 0
    for i in range(7):
        if list_of_nums[i] % 5 == 0 or list_of_nums[i] % 6 == 0:
            result += list_of_nums[i]
    return result