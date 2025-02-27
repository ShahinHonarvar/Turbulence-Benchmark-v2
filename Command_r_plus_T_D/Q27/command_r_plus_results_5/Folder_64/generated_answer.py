def insert_after_index(input_list):
    index_eight = input_list.index(8) + 1
    return input_list[:index_eight] + [3, 8] + input_list[index_eight:]