def all_pos_ints_exclusive(int_list):
    if len(int_list) < 52 or len(set(int_list)) != len(int_list) or (not all((isinstance(i, int) for i in int_list))):
        return []
    else:
        return [i for i in int_list[20:52] if i > 0]