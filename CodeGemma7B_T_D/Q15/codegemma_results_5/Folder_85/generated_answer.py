def sum_odd_ints_inclusive(the_list):
    accum = 0
    for i in range(6, 9):
        if the_list[i] % 2 != 0:
            accum += the_list[i]
    if accum == 0:
        return 0
    return accum