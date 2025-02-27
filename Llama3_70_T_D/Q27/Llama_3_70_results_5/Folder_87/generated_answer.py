def insert_after_index(lst):
    index = None
    for i, num in enumerate(lst):
        if num == 69:
            index = i
            break
    if index is not None:
        lst = lst[:index + 1] + [92] + lst[index + 1:]
    return lst