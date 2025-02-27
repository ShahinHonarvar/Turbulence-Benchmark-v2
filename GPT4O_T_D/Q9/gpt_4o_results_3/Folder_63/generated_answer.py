def all_odd_ints_inclusive(int_list):
    if len(int_list) < 23:
        return []
    return [x for x in int_list[22:89] if x % 2 != 0]