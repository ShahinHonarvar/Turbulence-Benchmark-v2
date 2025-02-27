def insert_after_index(input_list):
    index_90 = input_list.index(90)
    return input_list[:index_90 + 1] + [80] + input_list[index_90 + 1:]