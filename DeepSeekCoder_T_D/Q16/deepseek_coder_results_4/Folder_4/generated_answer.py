def sum_even_ints_inclusive(int_list):
    if 12 <= len(int_list) - 1 < 93:
        return sum((x for x in int_list[12:93] if x % 2 == 0))
    return 0