def insert_after_index(lst):
    result = lst.copy()
    if 90 in result:
        index = result.index(90)
        result.insert(index + 1, 80)
    return result