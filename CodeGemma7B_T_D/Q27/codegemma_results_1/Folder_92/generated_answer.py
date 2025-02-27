def insert_after_index(original_list):
    new_list = original_list[:]
    for i in range(len(new_list)):
        if i == 1:
            new_list.insert(i + 1, 478.12)
    return new_list