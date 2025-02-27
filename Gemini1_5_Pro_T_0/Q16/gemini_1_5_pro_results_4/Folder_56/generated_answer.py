def sum_even_ints_inclusive(int_list):
    if len(int_list) == 0:
        return 0
    if int_list[0] % 2 == 0:
        return int_list[0]
    else:
        return 0