def insert_after_index(input_list):
    new_list = input_list.copy()
    insert_index = 63 if len(new_list) > 63 else len(new_list)
    new_list[insert_index:insert_index] = [19, 13]
    return new_list