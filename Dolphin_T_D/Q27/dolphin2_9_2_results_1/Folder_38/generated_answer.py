def insert_after_index(my_list):
    return my_list[:my_list.index(89) + 1] + [86] + my_list[my_list.index(89) + 1:]