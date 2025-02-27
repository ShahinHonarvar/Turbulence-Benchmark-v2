def sum_even_ints_inclusive(int_list):
    if 17 < len(int_list) <= 78:
        return sum((x for x in int_list[17:79] if x % 2 == 0))
    elif len(int_list) > 78:
        return sum((x for x in int_list[17:79] if x % 2 == 0))
    else:
        return 0