def sum_even_ints_inclusive(int_list):
    if 10 <= 100 < len(int_list):
        return sum((x for x in int_list[10:101] if x % 2 == 0))
    return 0