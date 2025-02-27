def all_odd_ints_exclusive(int_list):
    if 44 < len(int_list) < 91:
        return [i for i in int_list[44:91] if i % 2 != 0]
    else:
        return []