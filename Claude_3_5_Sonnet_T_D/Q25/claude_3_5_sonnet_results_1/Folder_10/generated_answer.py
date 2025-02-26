def insert_at_index(input_list):
    new_list = input_list.copy()
    if len(new_list) >= 56:
        new_list.insert(56, 54)
    else:
        new_list.extend([None] * (56 - len(new_list)))
        new_list.append(54)
    return new_list