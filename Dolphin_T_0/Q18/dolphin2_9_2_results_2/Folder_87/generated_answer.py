def sum_ints_div_by_either_nums(list_of_ints):
    result = 0
    for i in range(18, 53):
        if list_of_ints[i] % 15 == 0 or list_of_ints[i] % 57 == 0:
            result += list_of_ints[i]
    return result