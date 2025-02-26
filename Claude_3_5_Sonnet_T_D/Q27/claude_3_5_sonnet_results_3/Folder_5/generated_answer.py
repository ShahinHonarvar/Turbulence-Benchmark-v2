def insert_after_index(input_list):
    new_list = input_list.copy()
    index_to_insert = 99 + 1
    if index_to_insert <= len(new_list):
        new_list.insert(index_to_insert, 15)
    else:
        new_list.append(15)
    return new_list