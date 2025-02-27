def insert_after_index(input_list):
    if len(input_list) > 44:
        return input_list[:45] + [76] + input_list[45:]
    else:
        return input_list + [76]