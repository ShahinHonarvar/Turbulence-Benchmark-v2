def insert_after_index(input_list):
    try:
        index = input_list.index(66)
        new_list = input_list[:index + 1] + [45] + input_list[index + 1:]
        return new_list
    except ValueError:
        return input_list + [45]