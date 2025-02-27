def sum_odd_ints_inclusive(int_list):
    if len(int_list) > 4:
        if int_list[4] % 2 != 0:
            return int_list[4]
    return 0