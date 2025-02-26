def insert_after_index(input_list):
    new_list = input_list.copy()
    insert_index = 33 if len(new_list) > 33 else len(new_list)
    new_list[insert_index:insert_index] = [54, 96]
    return new_list