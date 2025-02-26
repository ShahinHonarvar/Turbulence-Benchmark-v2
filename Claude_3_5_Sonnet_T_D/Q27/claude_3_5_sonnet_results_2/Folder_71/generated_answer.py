def insert_after_index(input_list):
    index_70 = input_list.index(70) if 70 in input_list else -1
    if index_70 != -1:
        return input_list[:index_70 + 1] + [76] + input_list[index_70 + 1:]
    else:
        return input_list