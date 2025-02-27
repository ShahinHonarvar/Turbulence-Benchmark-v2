def all_odd_ints_inclusive(int_list):
    if len(int_list) < 5:
        return []
    return [i for i in int_list[4:6] if i % 2 != 0]