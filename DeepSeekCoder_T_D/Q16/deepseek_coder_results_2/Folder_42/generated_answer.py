def sum_even_ints_inclusive(int_list):
    if 29 <= len(int_list) - 1 < 79:
        return sum((x for x in int_list[29:80] if x % 2 == 0))
    elif len(int_list) - 1 >= 79:
        return sum((x for x in int_list[29:80] if x % 2 == 0))
    else:
        return 0