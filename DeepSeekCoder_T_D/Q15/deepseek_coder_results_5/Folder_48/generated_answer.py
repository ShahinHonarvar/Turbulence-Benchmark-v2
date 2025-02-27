def sum_odd_ints_inclusive(int_list):
    if 533 <= len(int_list) - 1 < 605:
        return sum((x for x in int_list[533:606] if x % 2 != 0))
    elif len(int_list) - 1 >= 605:
        return sum((x for x in int_list[533:606] if x % 2 != 0))
    else:
        return 0