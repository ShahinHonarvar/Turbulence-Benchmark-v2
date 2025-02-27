def sum_odd_ints_inclusive(int_list):
    return sum((n for n in int_list[21:98:2] if n % 2 != 0))