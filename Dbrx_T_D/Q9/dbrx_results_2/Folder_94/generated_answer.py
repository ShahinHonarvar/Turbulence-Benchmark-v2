def all_odd_ints_inclusive(int_list):
    if len(int_list) < 41:
        return []
    else:
        return [i for i in int_list[28:41] if i % 2 != 0]