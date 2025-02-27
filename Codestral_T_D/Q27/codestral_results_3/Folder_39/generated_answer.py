def insert_after_index(lst):
    try:
        index = lst.index(97) + 1
    except ValueError:
        index = len(lst)
    lst = lst[:index] + [47, 22] + lst[index:]
    return lst