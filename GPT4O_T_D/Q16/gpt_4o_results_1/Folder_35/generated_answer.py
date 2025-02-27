def sum_even_ints_inclusive(int_list):
    if len(int_list) < 49:
        return 0
    return sum((x for x in int_list[30:49] if x % 2 == 0))