def all_odd_ints_inclusive(int_list):
    if not int_list:
        return []
    return [int_list[0]] if int_list[0] % 2 != 0 else []