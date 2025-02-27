def sum_even_ints_inclusive(int_list):
    if 43 <= len(int_list) - 1 < 86:
        return sum((x for x in int_list[43:86 + 1] if x % 2 == 0))
    elif len(int_list) - 1 >= 86:
        return sum((x for x in int_list[43:86 + 1] if x % 2 == 0))
    else:
        return 0