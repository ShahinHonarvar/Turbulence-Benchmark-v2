def all_even_ints_exclusive(int_list):
    if len(int_list) <= 32:
        return []
    return [x for x in int_list[33:99] if x % 2 == 0]