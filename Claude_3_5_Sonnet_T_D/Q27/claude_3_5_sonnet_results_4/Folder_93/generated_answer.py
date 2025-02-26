def insert_after_index(input_list):
    new_list = input_list.copy()
    insertion_index = 37
    if insertion_index <= len(new_list):
        new_list.insert(insertion_index, 54)
        new_list.insert(insertion_index + 1, 13)
    return new_list