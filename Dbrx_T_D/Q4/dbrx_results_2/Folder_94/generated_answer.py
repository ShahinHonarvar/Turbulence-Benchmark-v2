def all_pos_ints_exclusive(int_list):
    try:
        pos_ints = [i for i in int_list[28:53] if i > 0]
        return pos_ints
    except IndexError:
        return []