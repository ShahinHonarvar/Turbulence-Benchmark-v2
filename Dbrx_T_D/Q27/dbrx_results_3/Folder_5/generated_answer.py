def insert_after_index(lst):
    index = 99
    if index + 1 < len(lst):
        lst.insert(index + 1, 15)
    else:
        lst.append(15)
    return lst