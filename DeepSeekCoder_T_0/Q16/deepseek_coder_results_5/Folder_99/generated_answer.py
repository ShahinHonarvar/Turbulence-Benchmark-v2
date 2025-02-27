def sum_even_ints_inclusive(int_list):
    if 310 <= 370 < len(int_list):
        return sum((x for x in int_list[310:371] if x % 2 == 0))
    return 0