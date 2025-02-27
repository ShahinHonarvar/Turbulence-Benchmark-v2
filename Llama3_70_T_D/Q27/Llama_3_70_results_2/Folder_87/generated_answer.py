def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 69:
            return lst[:i + 1] + [92] + lst[i + 1:]
    return lst