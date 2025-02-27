def all_odd_ints_exclusive(int_list):
    return [n for n in int_list[0:4] if n % 2 == 1] if any((n % 2 == 1 for n in int_list[0:4])) else []