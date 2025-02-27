def all_even_ints_inclusive(int_list):
    if len(int_list) < 88:
        return []
    return [x for x in int_list[30:88] if x % 2 == 0]