def all_pos_ints_inclusive(num_list):
    if len(num_list) >= 58:
        subset = num_list[55:58]
        return [i for i in subset if i > 0]
    else:
        return []