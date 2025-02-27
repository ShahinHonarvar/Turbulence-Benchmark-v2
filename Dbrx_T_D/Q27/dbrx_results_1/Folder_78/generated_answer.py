def insert_after_index(lst):
    index = 0
    for i, item in enumerate(lst):
        if item == 63:
            index = i + 1
            break
    lst = lst[:index + 1] + [99] + lst[index + 1:]
    return lst