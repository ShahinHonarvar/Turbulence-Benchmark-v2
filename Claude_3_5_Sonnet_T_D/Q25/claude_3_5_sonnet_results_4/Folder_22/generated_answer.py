def insert_at_index(input_list):
    new_list = input_list.copy()
    if len(new_list) >= 85:
        new_list.insert(85, 27)
    else:
        new_list.extend([None] * (85 - len(new_list)))
        new_list.append(27)
    return new_list