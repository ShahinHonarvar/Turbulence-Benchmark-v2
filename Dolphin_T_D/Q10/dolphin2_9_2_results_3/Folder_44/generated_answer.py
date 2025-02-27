def all_odd_ints_exclusive(dummy_list):
    return [x for i, x in enumerate(dummy_list) if i > 81 and i < 86 and (x % 2 != 0)]