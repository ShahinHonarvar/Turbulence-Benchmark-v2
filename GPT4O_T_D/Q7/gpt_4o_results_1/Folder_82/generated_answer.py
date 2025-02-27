def all_even_ints_inclusive(int_list):
    if len(int_list) < 21:
        return []
    return [x for x in int_list[20:201] if x % 2 == 0]