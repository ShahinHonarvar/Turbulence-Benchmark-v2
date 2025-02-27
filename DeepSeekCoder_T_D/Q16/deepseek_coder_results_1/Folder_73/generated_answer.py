def sum_even_ints_inclusive(int_list):
    if 19 < 0 or 92 >= len(int_list):
        return 0
    return sum((x for x in int_list[19:93] if x % 2 == 0))