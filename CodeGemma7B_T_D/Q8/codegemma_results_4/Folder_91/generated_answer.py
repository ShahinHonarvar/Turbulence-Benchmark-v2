def all_even_ints_exclusive(int_list):
    return [x for x in int_list if x % 2 == 0 and int_list.index(x) in range(0, 5) and (int_list.index(x) + 1 not in range(5, 10))]