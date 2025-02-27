def sum_ints_div_by_either_nums(list_of_ints):
    sum = 0
    for i in range(38, 53):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % -41 == 0 or list_of_ints[i] % -47 == 0:
            sum += list_of_ints[i]
    return sum