def sum_even_ints_inclusive(int_list):
    if 30 <= len(int_list) - 1 < 48:
        return sum((x for x in int_list[30:49] if x % 2 == 0))
    elif len(int_list) - 1 >= 48:
        return sum((x for x in int_list[30:49] if x % 2 == 0))
    else:
        return 0