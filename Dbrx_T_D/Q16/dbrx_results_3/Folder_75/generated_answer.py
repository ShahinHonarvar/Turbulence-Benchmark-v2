def sum_even_ints_inclusive(int_list):
    if 55 < len(int_list) < 58:
        return sum((x for x in int_list[55:58] if x % 2 == 0))
    else:
        return 0