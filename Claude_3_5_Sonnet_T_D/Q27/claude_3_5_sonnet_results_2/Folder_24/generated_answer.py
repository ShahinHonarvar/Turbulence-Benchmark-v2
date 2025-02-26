def insert_after_index(input_list):
    new_list = input_list.copy()
    for i in range(len(new_list)):
        if i == 42:
            new_list.insert(i + 1, 53)
            break
    return new_list