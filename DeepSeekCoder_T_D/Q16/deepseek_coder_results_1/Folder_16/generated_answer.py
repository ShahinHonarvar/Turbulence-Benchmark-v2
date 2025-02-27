def sum_even_ints_inclusive(int_list):
    if 36 >= len(int_list) > 33:
        return sum((x for x in int_list[33:37] if x % 2 == 0))
    return 0