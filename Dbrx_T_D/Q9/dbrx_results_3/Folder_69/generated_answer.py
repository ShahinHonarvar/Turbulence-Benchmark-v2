def all_odd_ints_inclusive(int_list):
    if len(int_list) < 35:
        return []
    return [i for i in int_list[32:36] if i % 2 != 0]