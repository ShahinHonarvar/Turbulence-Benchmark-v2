def sum_even_ints_inclusive(int_list):
    if 30 <= len(int_list) - 1 < 48:
        return 0
    return sum((x for x in int_list[30:49] if x % 2 == 0))