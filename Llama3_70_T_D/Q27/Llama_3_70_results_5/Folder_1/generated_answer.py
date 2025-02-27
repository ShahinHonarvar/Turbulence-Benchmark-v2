def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 93:
            return lst[:i + 1] + [33, 78] + lst[i + 1:]
    return lst