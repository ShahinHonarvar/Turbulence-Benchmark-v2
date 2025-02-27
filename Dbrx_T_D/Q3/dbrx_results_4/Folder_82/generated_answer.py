def all_pos_ints_inclusive(int_list):
    if 20 > len(int_list) or 200 > len(int_list):
        return []
    else:
        return [i for i in int_list[20:201] if i > 0]