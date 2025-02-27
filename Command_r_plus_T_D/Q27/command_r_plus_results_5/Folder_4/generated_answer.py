def insert_after_index(my_list):
    insert_index = my_list.index(60) + 1
    return my_list[:insert_index] + [80, 74] + my_list[insert_index:]