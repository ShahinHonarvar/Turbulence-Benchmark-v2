def sum_odd_ints_inclusive(int_list):
    if 14 <= len(int_list) - 1 < 64:
        return sum((x for x in int_list[14:65] if x % 2 != 0))
    elif len(int_list) - 1 >= 64:
        return sum((x for x in int_list[14:65] if x % 2 != 0))
    else:
        return 0