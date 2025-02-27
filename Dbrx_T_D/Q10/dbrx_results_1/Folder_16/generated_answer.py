def all_odd_ints_exclusive(int_list):
    if len(int_list) < 90:
        return []
    else:
        return [i for i in int_list[86:90] if i % 2 != 0]