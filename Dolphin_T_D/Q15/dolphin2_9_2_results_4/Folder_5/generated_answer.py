def sum_odd_ints_inclusive(lst_of_ints):
    sum = 0
    if 8 < len(lst_of_ints) < 10:
        if lst_of_ints[8] % 2 != 0:
            sum += lst_of_ints[8]
        if lst_of_ints[9] % 2 != 0:
            sum += lst_of_ints[9]
    return sum