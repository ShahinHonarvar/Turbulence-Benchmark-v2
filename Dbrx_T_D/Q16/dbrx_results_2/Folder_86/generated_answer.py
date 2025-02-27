def sum_even_ints_inclusive(int_list):
    if len(int_list) < 35:
        return 0
    else:
        return sum((x for x in int_list[31:36] if x % 2 == 0))