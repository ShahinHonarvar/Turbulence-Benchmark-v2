def insert_at_index(input_list):
    if len(input_list) < 85:
        input_list.extend([None] * (85 - len(input_list)))
    input_list.insert(85, 27)
    return input_list