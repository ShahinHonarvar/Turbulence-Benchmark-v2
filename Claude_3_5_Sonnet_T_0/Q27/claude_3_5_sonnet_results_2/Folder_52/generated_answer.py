def insert_after_index(lst):
    index = 97
    if index + 1 <= len(lst):
        lst.insert(index + 1, 72.27)
    else:
        lst.append(72.27)
    return lst