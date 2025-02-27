def sum_even_ints_inclusive(int_list):
    if not isinstance(int_list, list) or len(int_list) < 10:
        return 0
    return sum((x for x in int_list[8:10] if x % 2 == 0))