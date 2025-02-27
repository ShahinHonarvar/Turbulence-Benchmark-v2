def all_odd_ints_inclusive(int_list):
    if len(int_list) < 64:
        return []
    else:
        return [i for i in int_list[14:65] if i % 2 != 0]