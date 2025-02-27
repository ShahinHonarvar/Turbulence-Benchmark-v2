def insert_after_index(a_list):
    index_to_insert = 585
    element_to_insert = 993.71
    return a_list[:index_to_insert + 1] + [element_to_insert] + a_list[index_to_insert + 1:]