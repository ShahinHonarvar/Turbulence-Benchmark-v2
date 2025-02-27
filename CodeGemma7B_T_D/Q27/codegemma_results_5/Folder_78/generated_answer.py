def insert_after_index(list):
    for i in list[:]:
        if i == list[63]:
            list.insert(i + 1, 99)
    return list