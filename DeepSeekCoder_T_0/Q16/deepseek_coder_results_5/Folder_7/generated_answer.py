def sum_even_ints_inclusive(int_list):
    if 661 <= 924 < len(int_list):
        return sum((x for x in int_list[661:925] if x % 2 == 0))
    return 0