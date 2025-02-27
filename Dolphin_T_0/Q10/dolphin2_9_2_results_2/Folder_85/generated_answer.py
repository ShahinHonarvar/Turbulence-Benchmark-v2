def all_odd_ints_exclusive(a_list):
    return [value for index, value in enumerate(a_list) if 4 < index < 5 and value % 2 != 0]