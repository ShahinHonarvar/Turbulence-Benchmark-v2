def insert_after_index(input_list):
    new_list = input_list.copy()
    insert_index = 37
    if insert_index <= len(new_list):
        new_list[insert_index:insert_index] = [54, 13]
    return new_list