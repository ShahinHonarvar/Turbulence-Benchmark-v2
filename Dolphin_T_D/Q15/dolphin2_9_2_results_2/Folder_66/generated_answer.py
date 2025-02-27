def sum_odd_ints_inclusive(int_list):
    return sum((x for i, x in enumerate(int_list[50:55]) if i % 2 == 1))