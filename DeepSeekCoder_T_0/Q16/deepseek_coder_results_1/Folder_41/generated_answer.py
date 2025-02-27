def sum_even_ints_inclusive(int_list):
    if 6 < len(int_list):
        return sum((x for x in int_list[6:7] if x % 2 == 0))
    return 0