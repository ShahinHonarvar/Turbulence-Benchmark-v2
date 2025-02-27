def sum_ints_div_by_either_nums(lst_ints):
    sum = 0
    for i in range(3):
        if lst_ints[i] % -2 == 0 or lst_ints[i] % 3 == 0:
            sum += lst_ints[i]
    return sum