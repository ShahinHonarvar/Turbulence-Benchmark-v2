def all_odd_ints_inclusive(int_list):
    if len(int_list) > 10:
        return [x for x in int_list[10:11] if x % 2 != 0]
    return []