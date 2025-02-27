def insert_after_index(lst):
    index = 63
    if index < len(lst):
        lst = lst[:index + 1] + [99] + lst[index + 1:]
    return lst