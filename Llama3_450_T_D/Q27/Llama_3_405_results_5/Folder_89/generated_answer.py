def insert_after_index(input_list):
    index = input_list.index(62)
    return input_list[:index + 1] + [51] + input_list[index + 1:]