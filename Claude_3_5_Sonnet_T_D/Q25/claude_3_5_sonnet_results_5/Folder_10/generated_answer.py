def insert_at_index(input_list):
    result_list = input_list.copy()
    if len(result_list) >= 56:
        result_list.insert(56, 54)
    else:
        result_list.extend([None] * (56 - len(result_list)) + [54])
    return result_list