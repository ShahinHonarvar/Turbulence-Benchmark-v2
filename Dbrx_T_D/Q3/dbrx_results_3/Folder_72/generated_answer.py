def all_pos_ints_inclusive(input_list):
    if len(input_list) < 52:
        return []
    else:
        return [x for x in input_list[29:52] if x > 0]