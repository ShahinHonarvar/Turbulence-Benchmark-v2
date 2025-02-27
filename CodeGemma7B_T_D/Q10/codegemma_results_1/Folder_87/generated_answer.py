def all_odd_ints_exclusive(int_list):
    filtered_list = [x for x in int_list[32:99] if x % 2 != 0]
    return filtered_list or []