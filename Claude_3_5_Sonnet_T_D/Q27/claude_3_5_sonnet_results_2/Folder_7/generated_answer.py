def insert_after_index(input_list):
    target_index = input_list.index(323)
    return input_list[:target_index + 1] + [389, 303] + input_list[target_index + 1:]