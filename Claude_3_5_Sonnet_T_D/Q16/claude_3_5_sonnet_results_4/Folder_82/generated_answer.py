def sum_even_ints_inclusive(int_list):
    if len(int_list) <= 29:
        return 0
    if int_list[29] % 2 == 0:
        return int_list[29]
    return 0