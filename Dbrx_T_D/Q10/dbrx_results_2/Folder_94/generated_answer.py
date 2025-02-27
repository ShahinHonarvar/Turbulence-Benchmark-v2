def all_odd_ints_exclusive(int_list):
    if len(int_list) < 54 or 28 > len(int_list):
        return []
    else:
        return [i for i in int_list[28:53] if i % 2 != 0]