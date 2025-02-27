def sum_odd_ints_inclusive(int_list):
    if not int_list or not isinstance(int_list[0], int):
        return 0
    return int_list[0] if int_list[0] % 2 != 0 else 0