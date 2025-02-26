def insert_at_index(input_list):
    result_list = input_list.copy()
    if len(result_list) >= 66:
        result_list.insert(66, 45)
    else:
        result_list.extend([None] * (66 - len(result_list)))
        result_list.append(45)
    return result_list