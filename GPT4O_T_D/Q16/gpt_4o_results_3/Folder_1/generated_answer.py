def sum_even_ints_inclusive(int_list):
    if len(int_list) < 73:
        return 0
    return sum((i for i in int_list[31:73] if i % 2 == 0))