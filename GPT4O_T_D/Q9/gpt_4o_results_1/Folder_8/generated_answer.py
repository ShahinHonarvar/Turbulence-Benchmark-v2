def all_odd_ints_inclusive(int_list):
    if len(int_list) < 24:
        return []
    return [x for x in int_list[23:24] if x % 2 != 0]