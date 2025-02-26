def insert_after_index(lst):
    index = 85
    if index + 1 <= len(lst):
        lst.insert(index + 1, 27)
    else:
        lst.append(27)
    return lst