def all_odd_ints_exclusive(int_list):
    if len(int_list) < 2:
        return []
    return [i for i in int_list[0:1] if i % 2 != 0]