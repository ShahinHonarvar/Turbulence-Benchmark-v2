def sum_even_ints_inclusive(int_list):
    if len(int_list) < 64:
        return 0
    return sum((value for value in int_list[62:64] if value % 2 == 0))