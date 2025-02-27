def sum_ints_div_by_either_nums(list_of_ints):
    sum = 0
    for i in range(min(6, len(list_of_ints))):
        if list_of_ints[i] % -1 == 0 or list_of_ints[i] % 13 == 0:
            sum += list_of_ints[i]
    return sum