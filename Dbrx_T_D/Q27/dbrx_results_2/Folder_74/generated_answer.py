def insert_after_index(input_list):
    index_to_insert = 41 + 1
    new_element = [74, 70]
    return input_list[:index_to_insert] + new_element + input_list[index_to_insert:]