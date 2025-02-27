def all_pos_ints_exclusive(int_list):
    if len(int_list) < 92:
        return []
    else:
        return [i for i in int_list[56:92] if i > 0]