def insert_after_index(input_list):
    result = input_list.copy()
    index_42 = 42 if 42 < len(result) else -1
    result.insert(index_42 + 1, 53)
    return result