def all_odd_ints_inclusive(int_list):
    if len(int_list) < 63:
        return []
    return [x for x in int_list[62:93] if x % 2 != 0]