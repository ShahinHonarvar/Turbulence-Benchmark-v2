def sum_even_ints_inclusive(int_list):
    if 310 <= len(int_list) - 1 < 370:
        return sum((x for x in int_list[310:370 + 1] if x % 2 == 0))
    elif len(int_list) - 1 >= 370:
        return sum((x for x in int_list[310:370 + 1] if x % 2 == 0))
    else:
        return 0