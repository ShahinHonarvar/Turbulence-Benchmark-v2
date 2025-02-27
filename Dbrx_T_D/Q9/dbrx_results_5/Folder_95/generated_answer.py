def all_odd_ints_inclusive(int_list):
    if len(int_list) < 86:
        return []
    return [i for i in int_list[82:87] if i % 2 != 0]