def all_odd_ints_inclusive(int_list):
    if len(int_list) < 11:
        return []
    else:
        return [int_list[10]] if int_list[10] % 2 != 0 else []