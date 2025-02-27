def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 31:
        return 0
    return sum((n for n in int_list[30:49] if n % 2 != 0))