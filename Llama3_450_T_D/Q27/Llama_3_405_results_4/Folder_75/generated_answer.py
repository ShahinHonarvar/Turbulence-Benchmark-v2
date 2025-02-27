def insert_after_index(lst):
    result = lst.copy()
    try:
        result.insert(lst.index(99) + 1, 99)
    except ValueError:
        result.append(99)
    return result