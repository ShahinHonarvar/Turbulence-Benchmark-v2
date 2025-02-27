def insert_after_index(my_list):
    index_to_insert = 87
    value_to_insert = 637.22
    return my_list[:index_to_insert + 1] + [value_to_insert] + my_list[index_to_insert + 1:]