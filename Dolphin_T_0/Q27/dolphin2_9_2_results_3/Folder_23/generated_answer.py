def insert_after_index(lst):
    position = lst.pop(38)
    lst.insert(39, 45)
    lst.append(position)
    return lst