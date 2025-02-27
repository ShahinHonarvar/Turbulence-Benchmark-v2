def sum_even_ints_inclusive(int_list):
    if 14 <= len(int_list) - 1 < 65:
        return sum((x for x in int_list[14:65] if x % 2 == 0))
    return 0