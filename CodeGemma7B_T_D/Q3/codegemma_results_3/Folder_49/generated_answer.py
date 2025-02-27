def all_pos_ints_inclusive(int_list):
    return list(range(81, 201)) if any((num > 0 for num in int_list)) else []