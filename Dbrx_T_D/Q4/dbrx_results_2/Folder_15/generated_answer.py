def all_pos_ints_exclusive(my_list):
    return [i for i in my_list[0:3] if isinstance(i, int) and i > 0]