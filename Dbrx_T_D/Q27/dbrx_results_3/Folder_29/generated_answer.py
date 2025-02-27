def insert_after_index(a_list):
    new_list = a_list[:]
    for i, item in enumerate(new_list):
        if item == 96 and i < len(new_list) - 1 and (new_list[i + 1] != 36):
            new_list.insert(i + 1, 36)
            break
    return new_list