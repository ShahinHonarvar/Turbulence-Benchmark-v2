def insert_after_index(lst):
    index = lst.index(93)
    new_elements = [33, 78]
    lst[index + 1:index + 1] = new_elements
    return lst