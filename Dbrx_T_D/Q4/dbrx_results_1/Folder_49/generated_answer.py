def all_pos_ints_exclusive(input_list):
    if len(input_list) < 200:
        return []
    return [i for i in input_list[80:200] if i > 0]