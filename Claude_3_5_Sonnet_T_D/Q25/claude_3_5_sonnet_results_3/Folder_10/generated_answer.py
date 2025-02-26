def insert_at_index(input_list):
    if len(input_list) >= 56:
        return input_list[:56] + [54] + input_list[56:]
    else:
        return input_list + [None] * (56 - len(input_list)) + [54]