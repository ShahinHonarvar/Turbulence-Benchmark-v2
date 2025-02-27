def sum_even_ints_inclusive(int_list):
    if len(int_list) < 100:
        return 0
    return sum((i for i in int_list[91:100] if i % 2 == 0))