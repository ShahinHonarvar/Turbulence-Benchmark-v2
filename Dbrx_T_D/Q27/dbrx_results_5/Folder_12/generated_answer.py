def insert_after_index(lst):
    index = None
    for i in range(len(lst)):
        if lst[i] == 57:
            index = i
            break
    if index is not None:
        lst = lst[:index + 1] + [96] + lst[index + 1:]
    return lst