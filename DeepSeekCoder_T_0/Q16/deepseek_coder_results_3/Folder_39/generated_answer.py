def sum_even_ints_inclusive(int_list):
    if 20 < len(int_list) <= 30:
        return sum((x for x in int_list[20:31] if x % 2 == 0))
    elif len(int_list) > 30:
        return sum((x for x in int_list[20:31] if x % 2 == 0))
    else:
        return 0