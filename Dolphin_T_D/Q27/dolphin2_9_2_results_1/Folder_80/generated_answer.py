def insert_after_index(lst):
    index = lst.index(95)
    if index == len(lst) - 1:
        lst.append(43)
    else:
        lst.insert(index + 1, 43)
    return lst