def sum_even_ints_inclusive(int_list):
    if 661 < len(int_list) <= 924:
        return sum((x for x in int_list[661:925] if x % 2 == 0))
    elif len(int_list) > 924:
        return sum((x for x in int_list[661:925] if x % 2 == 0))
    else:
        return 0