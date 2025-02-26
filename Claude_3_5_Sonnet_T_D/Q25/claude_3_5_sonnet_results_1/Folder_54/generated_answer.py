def insert_at_index(input_list):
    result_list = input_list.copy()
    if len(result_list) >= 43:
        result_list.insert(43, 37)
    else:
        result_list.extend([None] * (43 - len(result_list)))
        result_list.append(37)
    return result_list