def sum_even_ints_inclusive(int_list):
    if 29 <= len(int_list) - 1 < 51:
        return sum((x for x in int_list[29:51] if x % 2 == 0))
    elif len(int_list) - 1 >= 51:
        return sum((x for x in int_list[29:52] if x % 2 == 0))
    else:
        return 0