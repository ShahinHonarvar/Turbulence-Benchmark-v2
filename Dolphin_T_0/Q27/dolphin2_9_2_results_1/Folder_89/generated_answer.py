def insert_after_index(lst):
    result = list(lst)
    index = lst.index(62)
    result.insert(index + 1, 51)
    return result