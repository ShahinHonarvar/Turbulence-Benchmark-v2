def all_pos_ints_exclusive(input_list):
    if len(input_list) >= 8 and all((isinstance(i, int) for i in input_list)):
        return [i for i in input_list[3:8] if i > 0]
    else:
        return []