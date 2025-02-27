def all_even_ints_exclusive(int_list):
    if len(int_list) < 24:
        return []
    else:
        return [i for i in int_list[22:24] if i % 2 == 0]