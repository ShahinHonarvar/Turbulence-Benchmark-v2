def sum_odd_ints_inclusive(int_list):
    return sum((i for i in int_list[10:101] if i % 2 != 0))