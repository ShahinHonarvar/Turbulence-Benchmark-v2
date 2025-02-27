def insert_after_index(lst):
    index = lst.index(90)
    if index == len(lst) - 1:
        lst.append(80)
    else:
        lst.insert(index + 1, 80)
    return lst