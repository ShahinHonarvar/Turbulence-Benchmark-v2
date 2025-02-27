def all_odd_ints_exclusive(int_list):
    if len(int_list) < 5:
        return []
    else:
        return [i for i in int_list[0:5] if i % 2 != 0]