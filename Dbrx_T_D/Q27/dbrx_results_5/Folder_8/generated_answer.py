def insert_after_index(input_list):
    index_to_insert = None
    for i in range(len(input_list)):
        if input_list[i] == 57:
            index_to_insert = i + 1
            break
    if index_to_insert is not None:
        input_list = input_list[:index_to_insert] + [76] + input_list[index_to_insert:]
    return input_list