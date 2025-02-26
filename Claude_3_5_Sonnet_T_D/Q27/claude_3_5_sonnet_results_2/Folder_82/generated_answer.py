def insert_after_index(input_list):
    result_list = input_list.copy()
    insert_index = 85 if len(result_list) > 84 else len(result_list)
    result_list.insert(insert_index, 771.92)
    return result_list