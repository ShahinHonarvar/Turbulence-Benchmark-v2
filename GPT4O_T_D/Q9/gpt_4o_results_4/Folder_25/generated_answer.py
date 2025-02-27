def all_odd_ints_inclusive(int_list):
    if len(int_list) < 30:
        return []
    return [x for x in int_list[29:94] if x % 2 != 0]