def sum_even_ints_inclusive(int_list):
    if len(int_list) <= 63:
        return 0
    elif len(int_list) <= 62:
        return sum((x for x in int_list[62:] if x % 2 == 0))
    else:
        return sum((x for x in int_list[62:63] if x % 2 == 0))