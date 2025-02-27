def insert_after_index(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == 42:
            return lst[:i + 1] + [53] + lst[i + 1:]
    return lst + [53]