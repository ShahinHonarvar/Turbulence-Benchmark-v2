def insert_after_index(input_list):
    return input_list[:input_list.index(598) + 1] + [385, 999] + input_list[input_list.index(598) + 1:]