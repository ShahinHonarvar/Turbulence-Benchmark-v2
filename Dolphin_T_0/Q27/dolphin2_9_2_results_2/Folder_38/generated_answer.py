def insert_after_index(list):
    for i, item in enumerate(list):
        if item == 89:
            list.insert(i + 1, 86)
            break
    return list