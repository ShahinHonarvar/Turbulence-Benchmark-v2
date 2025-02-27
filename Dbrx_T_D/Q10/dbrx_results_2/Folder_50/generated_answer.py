def all_odd_ints_exclusive(int_list):
    if len(int_list) < 98:
        return []
    return [i for i in int_list[70:98] if i % 2 != 0]