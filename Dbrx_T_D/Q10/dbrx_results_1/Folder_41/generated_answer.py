def all_odd_ints_exclusive(int_list):
    if len(int_list) >= 10:
        return [i for i in int_list[8:9] if i % 2 != 0]
    else:
        return []