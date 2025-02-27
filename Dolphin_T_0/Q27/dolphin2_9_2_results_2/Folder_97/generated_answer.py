def insert_after_index(input_list):
    result = input_list[:500]
    result.extend([912, 170])
    result.extend(input_list[500:])
    return result