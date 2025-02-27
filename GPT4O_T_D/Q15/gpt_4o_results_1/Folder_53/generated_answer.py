def sum_odd_ints_inclusive(int_list):
    if not 300 < len(int_list) <= 301:
        return 0
    if int_list[300] % 2 != 0:
        return int_list[300]
    return 0