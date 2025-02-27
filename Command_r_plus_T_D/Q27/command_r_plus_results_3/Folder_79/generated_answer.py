def insert_after_index(input_list):
    insertion_index = 29
    insertion_elements = [41, 69]
    if insertion_index < len(input_list):
        input_list.insert(insertion_index, *insertion_elements)
    else:
        input_list.extend(insertion_elements)
    return input_list