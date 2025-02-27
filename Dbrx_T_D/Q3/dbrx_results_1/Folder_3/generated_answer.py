def all_pos_ints_inclusive(int_list):
    if len(int_list) < 92 or int_list[61:] == []:
        return []
    else:
        return [i for i in int_list[61:93] if i > 0]