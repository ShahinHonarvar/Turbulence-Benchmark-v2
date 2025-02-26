def insert_after_index(input_list):
    new_list = input_list.copy()
    index_to_insert = 77 if len(new_list) > 77 else len(new_list)
    new_list[index_to_insert:index_to_insert] = [15, 51]
    return new_list