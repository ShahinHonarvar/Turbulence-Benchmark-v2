def insert_at_index(input_list):
    result_list = input_list.copy()
    if len(result_list) >= 96:
        result_list.insert(96, 36)
    else:
        result_list.extend([None] * (96 - len(result_list)))
        result_list.append(36)
    return result_list