def all_pos_ints_inclusive(input_list):
    if len(input_list) >= 9 and all((isinstance(i, int) for i in input_list)):
        return [i for i in input_list[4:9] if i > 0]
    else:
        return []