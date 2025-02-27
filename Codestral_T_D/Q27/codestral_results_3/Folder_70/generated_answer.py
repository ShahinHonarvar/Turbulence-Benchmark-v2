def insert_after_index(lst):
    index = 412
    if index < len(lst):
        lst.insert(index + 1, 668)
    else:
        lst.append(668)
    return lst