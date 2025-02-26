def insert_after_index(input_list):
    target_index = 87
    insert_list = [78, 16]
    if target_index < len(input_list):
        input_list[target_index + 1:target_index + 1] = insert_list
    return input_list