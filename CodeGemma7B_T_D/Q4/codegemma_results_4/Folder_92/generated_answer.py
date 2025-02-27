def all_pos_ints_exclusive(num_list):
    return [n for n in range(num_list[0], num_list[1]) if n > 0] or []