def insert_at_index(input_list):
    result_list = input_list.copy()
    if len(result_list) < 90:
        result_list.extend([None] * (90 - len(result_list)))
    result_list.insert(89, 86)
    return result_list