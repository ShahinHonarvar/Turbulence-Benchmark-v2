def all_pos_ints_inclusive(num_list):
    if len(num_list) >= 88:
        return [i for i in num_list[25:88] if i > 0]
    else:
        return []