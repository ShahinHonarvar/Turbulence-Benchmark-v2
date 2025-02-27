def all_odd_ints_inclusive(int_list):
    if len(int_list) >= 35:
        return [i for i in int_list[30:35] if i % 2 != 0]
    else:
        return []