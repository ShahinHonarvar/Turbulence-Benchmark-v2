def all_odd_ints_exclusive(int_list):
    if len(int_list) < 40:
        return []
    return [i for i in int_list[15:40] if i % 2 != 0]