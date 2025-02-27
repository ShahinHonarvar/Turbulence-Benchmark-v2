def all_pos_ints_exclusive(input_list):
    if len(input_list) < 95:
        return []
    result = input_list[87:95]
    return [i for i in result if i > 0]