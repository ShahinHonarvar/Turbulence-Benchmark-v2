def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 35:
            return lst[:i + 1] + [90, 76] + lst[i + 1:]
    return lst