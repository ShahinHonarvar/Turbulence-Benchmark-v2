def sum_odd_ints_inclusive(n_list):
    n_list_sub = n_list[27:40]
    return sum((x for x in n_list_sub if x % 2 != 0))