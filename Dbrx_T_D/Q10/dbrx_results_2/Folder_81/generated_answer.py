def all_odd_ints_exclusive(int_list):
    if len(int_list) < 12:
        return []
    return [i for i in int_list[10:12] if i % 2 != 0]