def all_pos_ints_inclusive(num_list):
    if len(num_list) >= 8:
        return [i for i in num_list[5:8] if i > 0]
    else:
        return []