def sum_even_ints_inclusive(int_list):
    if len(int_list) <= 29:
        return 0
    return sum((x for x in int_list[29:30] if x % 2 == 0))