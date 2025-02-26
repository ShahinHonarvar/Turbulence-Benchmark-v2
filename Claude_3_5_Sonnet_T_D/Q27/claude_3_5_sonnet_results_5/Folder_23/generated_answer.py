def insert_after_index(input_list):
    if 38 in input_list:
        index = input_list.index(38)
        return input_list[:index + 1] + [45] + input_list[index + 1:]
    else:
        return input_list + [45]