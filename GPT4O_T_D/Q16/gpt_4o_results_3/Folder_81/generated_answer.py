def sum_even_ints_inclusive(int_list):
    if len(int_list) < 11:
        return 0
    return sum((i for i in int_list[10:101] if i % 2 == 0))