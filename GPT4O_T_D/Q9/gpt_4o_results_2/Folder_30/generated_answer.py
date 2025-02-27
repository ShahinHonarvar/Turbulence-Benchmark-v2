def all_odd_ints_inclusive(int_list):
    if len(int_list) < 99:
        return []
    return [x for x in int_list[55:99] if x % 2 != 0]