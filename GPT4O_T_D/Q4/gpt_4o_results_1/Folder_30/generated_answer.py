def all_pos_ints_exclusive(int_list):
    if len(int_list) <= 87:
        return []
    return [x for x in int_list[87:89] if x > 0]