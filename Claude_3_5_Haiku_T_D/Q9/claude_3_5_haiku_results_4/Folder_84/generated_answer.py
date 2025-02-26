def all_odd_ints_inclusive(int_list):
    if len(int_list) <= 86:
        return []
    return [x for x in int_list[43:87] if x % 2 != 0]