def insert_after_index(list):
    for idx, val in enumerate(list):
        if idx == 21:
            list.insert(idx + 1, 655.24)
    return list