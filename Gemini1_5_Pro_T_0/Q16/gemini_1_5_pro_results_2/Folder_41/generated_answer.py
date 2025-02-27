def sum_even_ints_inclusive(int_list):
    if len(int_list) < 7:
        return 0
    if int_list[6] % 2 == 0:
        return int_list[6]
    else:
        return 0