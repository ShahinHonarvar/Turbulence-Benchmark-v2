def sum_even_ints_inclusive(int_list):
    if 62 < len(int_list) <= 99:
        return sum((x for x in int_list[62:100] if x % 2 == 0))
    elif len(int_list) > 99:
        return sum((x for x in int_list[62:100] if x % 2 == 0))
    else:
        return 0