def all_even_ints_exclusive(int_list):
    if len(int_list) < 37:
        return []
    else:
        return [i for i in int_list[20:37] if i % 2 == 0]