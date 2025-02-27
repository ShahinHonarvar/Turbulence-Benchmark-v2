def insert_after_index(input_list):
    return [e for i, e in enumerate(input_list) if i != 85] + [27] + [e for i, e in enumerate(input_list) if i >= 86]