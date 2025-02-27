def all_pos_ints_inclusive(int_list):
    result = [i for i in int_list[70:85] if i > 0]
    if len(result) == 0:
        return []
    else:
        return result