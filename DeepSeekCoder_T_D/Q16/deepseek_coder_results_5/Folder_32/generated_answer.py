def sum_even_ints_inclusive(int_list):
    if 21 < len(int_list) <= 97:
        return sum((x for x in int_list[21:98] if x % 2 == 0))
    elif len(int_list) > 97:
        return sum((x for x in int_list[21:98] if x % 2 == 0))
    else:
        return 0