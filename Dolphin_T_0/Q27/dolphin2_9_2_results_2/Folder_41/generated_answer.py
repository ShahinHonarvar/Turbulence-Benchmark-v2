def insert_after_index(lst):
    result = lst[:]
    index = result.index(87) + 1
    result.insert(index, 78)
    result.insert(index + 1, 16)
    return result