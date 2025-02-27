def insert_after_index(lst):
    index = 76
    element = [15, 51]
    new_lst = lst[:]
    new_lst.insert(index + 1, element)
    return new_lst