def insert_after_index(input_list):
    new_list = input_list.copy()
    insert_index = 77 if len(new_list) > 76 else len(new_list)
    new_list[insert_index:insert_index] = [15, 51]
    return new_list