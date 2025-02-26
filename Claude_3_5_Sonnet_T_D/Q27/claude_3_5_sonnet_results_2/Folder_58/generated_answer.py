def insert_after_index(input_list):
    new_list = input_list.copy()
    insert_index = 599
    if insert_index <= len(new_list):
        new_list[insert_index:insert_index] = [385, 999]
    else:
        new_list.extend([385, 999])
    return new_list