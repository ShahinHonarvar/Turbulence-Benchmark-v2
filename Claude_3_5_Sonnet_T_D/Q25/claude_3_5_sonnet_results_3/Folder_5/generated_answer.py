def insert_at_index(input_list):
    result_list = input_list.copy()
    if len(result_list) > 99:
        result_list.insert(99, 15)
    else:
        result_list.extend([None] * (99 - len(result_list)) + [15])
    return result_list