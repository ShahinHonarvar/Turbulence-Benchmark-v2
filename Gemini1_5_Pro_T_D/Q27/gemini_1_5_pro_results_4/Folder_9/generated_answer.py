def insert_after_index(list_arg):
    try:
        index_of_66 = list_arg.index(66)
        updated_list = list_arg[:index_of_66 + 1] + [45] + list_arg[index_of_66 + 1:]
        return updated_list
    except:
        return list_arg