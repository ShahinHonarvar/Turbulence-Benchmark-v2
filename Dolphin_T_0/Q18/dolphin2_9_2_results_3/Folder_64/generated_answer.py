def sum_ints_div_by_either_nums(list_of_ints):
    result = 0
    for i in range(4):
        if list_of_ints[i] % 11 == 0 or list_of_ints[i] % -7 == 0:
            result += list_of_ints[i]
    return result