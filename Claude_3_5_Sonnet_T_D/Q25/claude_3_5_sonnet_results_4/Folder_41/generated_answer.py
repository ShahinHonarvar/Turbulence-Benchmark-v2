def insert_at_index(input_list):
    result_list = input_list.copy()
    if len(result_list) < 88:
        result_list.extend([None] * (88 - len(result_list)))
    result_list.insert(87, [78, 16])
    return result_list