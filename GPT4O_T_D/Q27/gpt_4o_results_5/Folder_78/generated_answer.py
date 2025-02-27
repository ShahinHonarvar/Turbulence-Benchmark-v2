def insert_after_index(input_list):
    if len(input_list) > 63:
        return input_list[:64] + [99] + input_list[64:]
    return input_list