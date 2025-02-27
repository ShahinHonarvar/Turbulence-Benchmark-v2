def sum_even_ints_inclusive(int_list):
    if 533 <= 605 < len(int_list):
        return sum((x for x in int_list[533:606] if x % 2 == 0))
    return 0