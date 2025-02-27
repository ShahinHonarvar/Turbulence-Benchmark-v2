def insert_after_index(num_list):
    for i, num in enumerate(num_list):
        if num == 99:
            num_list.insert(i + 1, 99)
    return num_list