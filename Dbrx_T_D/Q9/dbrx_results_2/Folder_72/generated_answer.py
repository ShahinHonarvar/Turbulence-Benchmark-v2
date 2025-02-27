def all_odd_ints_inclusive(int_list):
    if len(int_list) < 51:
        return []
    else:
        return [i for i in int_list[29:52] if i % 2 != 0]