def sum_odd_ints_inclusive(int_list):
    if 22 <= len(int_list) - 1 < 88:
        return sum((x for x in int_list[22:88 + 1] if x % 2 != 0))
    elif len(int_list) - 1 >= 88:
        return sum((x for x in int_list[22:88 + 1] if x % 2 != 0))
    else:
        return 0