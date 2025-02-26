def insert_at_index(input_list):
    if len(input_list) < 87:
        input_list.extend([None] * (87 - len(input_list)))
    return input_list[:87] + [78, 16] + input_list[87:]