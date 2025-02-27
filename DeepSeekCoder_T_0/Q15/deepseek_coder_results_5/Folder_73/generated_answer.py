def sum_odd_ints_inclusive(int_list):
    if 19 < len(int_list) <= 92:
        return sum((x for x in int_list[19:93] if x % 2 != 0))
    elif len(int_list) > 92:
        return sum((x for x in int_list[19:93] if x % 2 != 0))
    else:
        return 0