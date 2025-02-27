def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 96:
            lst = lst[:i + 1] + [36] + lst[i + 1:]
    return lst