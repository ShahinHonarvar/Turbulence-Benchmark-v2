def all_pos_ints_exclusive(input_list):
    if len(input_list) < 94:
        return []
    result = input_list[19:94]
    return [x for x in result if x > 0]