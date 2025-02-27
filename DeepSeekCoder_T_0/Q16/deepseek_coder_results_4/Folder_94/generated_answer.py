def sum_even_ints_inclusive(int_list):
    if 28 <= 40 < len(int_list):
        return sum((x for x in int_list[28:41] if x % 2 == 0))
    return 0