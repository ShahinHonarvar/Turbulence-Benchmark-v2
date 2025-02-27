def insert_after_index(lst):
    index = lst.index(60)
    result = lst[:index + 1] + [80, 74] + lst[index + 1:]
    return result