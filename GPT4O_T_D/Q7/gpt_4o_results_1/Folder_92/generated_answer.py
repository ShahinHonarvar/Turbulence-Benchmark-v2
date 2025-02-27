def all_even_ints_inclusive(int_list):
    if len(int_list) < 2:
        return []
    return [x for x in int_list[0:2] if x % 2 == 0]