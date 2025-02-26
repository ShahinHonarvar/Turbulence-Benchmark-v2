def insert_at_index(input_list):
    result = input_list.copy()
    if len(result) >= 95:
        result.insert(95, 43)
    else:
        result.extend([None] * (95 - len(result)))
        result.append(43)
    return result