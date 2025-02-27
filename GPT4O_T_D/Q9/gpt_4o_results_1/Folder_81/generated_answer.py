def all_odd_ints_inclusive(int_list):
    if len(int_list) < 11:
        return []
    return [x for x in int_list[10:101] if x % 2 != 0]