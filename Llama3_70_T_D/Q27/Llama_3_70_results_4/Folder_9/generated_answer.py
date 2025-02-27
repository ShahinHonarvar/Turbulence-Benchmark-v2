def insert_after_index(input_list):
    if len(input_list) > 66:
        return input_list[:67] + [45] + input_list[67:]
    else:
        return input_list + [45]