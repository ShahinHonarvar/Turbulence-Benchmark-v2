def insert_after_index(lst):
    index = 5
    if index >= len(lst):
        lst.append(7)
    else:
        lst = lst[:index] + [7] + lst[index:]
    return lst