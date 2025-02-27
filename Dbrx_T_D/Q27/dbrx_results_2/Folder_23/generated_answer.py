def insert_after_index(given_list):
    index_to_insert = 38
    element_to_insert = 45
    if index_to_insert < len(given_list) - 1:
        new_list = given_list[:index_to_insert + 1] + [element_to_insert] + given_list[index_to_insert + 1:]
    else:
        new_list = given_list[:index_to_insert + 1] + [element_to_insert]
    return new_list