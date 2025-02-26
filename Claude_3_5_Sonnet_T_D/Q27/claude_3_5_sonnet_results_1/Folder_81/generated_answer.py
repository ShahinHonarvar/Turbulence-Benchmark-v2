def insert_after_index(input_list):
    new_list = input_list.copy()
    for i in range(len(new_list)):
        if i == 28:
            new_list.insert(i + 1, 20)
            break
    return new_list