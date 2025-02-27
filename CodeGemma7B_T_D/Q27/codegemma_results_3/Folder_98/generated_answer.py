def insert_after_index(list):
    if len(list) <= 10:
        return None
    else:
        list.insert(10, 1)
        return list