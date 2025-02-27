def all_even_ints_exclusive(int_list):
    if len(int_list) <= 3:
        return []
    return [x for x in int_list[2:len(int_list) - 1] if x % 2 == 0]