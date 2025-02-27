def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 85:
            return lst[:i + 1] + [41, 95] + lst[i + 1:]
    return lst