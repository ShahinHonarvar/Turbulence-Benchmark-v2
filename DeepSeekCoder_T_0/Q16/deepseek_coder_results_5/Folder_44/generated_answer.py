def sum_even_ints_inclusive(int_list):
    if 13 <= len(int_list) - 1 < 68:
        return sum((x for x in int_list[13:68 + 1] if x % 2 == 0))
    elif len(int_list) - 1 >= 68:
        return sum((x for x in int_list[13:68 + 1] if x % 2 == 0))
    else:
        return 0