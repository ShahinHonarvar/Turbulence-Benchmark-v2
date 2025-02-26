def insert_after_index(given_list):
    index_to_insert = 38 + 1
    new_list = given_list[:index_to_insert] + [45] + given_list[index_to_insert:]
    return new_list