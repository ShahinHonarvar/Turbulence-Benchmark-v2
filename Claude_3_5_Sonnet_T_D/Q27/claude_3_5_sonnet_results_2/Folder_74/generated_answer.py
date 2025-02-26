def insert_after_index(input_list):
    new_list = input_list.copy()
    insert_index = 42 if len(new_list) > 42 else len(new_list)
    new_list[insert_index:insert_index] = [74, 70]
    return new_list