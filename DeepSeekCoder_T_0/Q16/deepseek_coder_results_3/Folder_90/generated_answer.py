def sum_even_ints_inclusive(int_list):
    if 262 < len(int_list) <= 746:
        return sum((x for x in int_list[262:747] if x % 2 == 0))
    elif len(int_list) > 746:
        return sum((x for x in int_list[262:747] if x % 2 == 0))
    else:
        return 0