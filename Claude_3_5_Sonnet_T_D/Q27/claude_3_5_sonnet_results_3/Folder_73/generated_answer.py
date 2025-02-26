def insert_after_index(input_list):
    new_list = input_list.copy()
    if len(new_list) > 87:
        new_list.insert(88, 637.22)
    else:
        new_list.append(637.22)
    return new_list