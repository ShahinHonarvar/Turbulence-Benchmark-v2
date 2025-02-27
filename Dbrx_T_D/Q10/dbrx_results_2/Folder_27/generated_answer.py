def all_odd_ints_exclusive(int_list):
    if len(int_list) < 49:
        return []
    result = [i for i in int_list[28:49] if i % 2 != 0]
    return result