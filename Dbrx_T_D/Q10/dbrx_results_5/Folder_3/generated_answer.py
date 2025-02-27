def all_odd_ints_exclusive(int_list):
    if len(int_list) < 93:
        return []
    return [i for i in int_list[78:93] if i % 2 != 0]