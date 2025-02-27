def all_even_ints_exclusive(my_list):
    return [x for i, x in enumerate(my_list) if 13 < i < 70 if x % 2 == 0]