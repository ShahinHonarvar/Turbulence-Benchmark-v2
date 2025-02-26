def insert_after_index(lst):
    result = lst.copy()
    try:
        index = result.index(90)
        result.insert(index + 1, 80)
    except ValueError:
        pass
    return result