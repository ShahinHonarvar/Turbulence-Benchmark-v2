def sum_even_ints_inclusive(int_list):
    if 75 <= len(int_list) - 1 < 88:
        return sum((x for x in int_list[75:88 + 1] if x % 2 == 0))
    elif len(int_list) - 1 >= 88:
        return sum((x for x in int_list[75:88 + 1] if x % 2 == 0))
    else:
        return 0