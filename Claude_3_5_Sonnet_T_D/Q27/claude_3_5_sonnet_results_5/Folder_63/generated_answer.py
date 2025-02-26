def insert_after_index(input_list):
    new_list = input_list.copy()
    insertion_index = 77
    if insertion_index <= len(new_list):
        new_list.insert(insertion_index, [15, 51])
    else:
        new_list.append([15, 51])
    return new_list