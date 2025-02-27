def sum_even_ints_inclusive(int_list):
    if len(int_list) < 77:
        return 0
    else:
        return sum((x for x in int_list[36:77] if x % 2 == 0))