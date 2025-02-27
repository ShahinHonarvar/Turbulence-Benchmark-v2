def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 70:
            return lst[:i + 1] + [76] + lst[i + 1:]
    return lst