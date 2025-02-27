def insert_after_index(lst):
    for i in range(len(lst)):
        if i == 100:
            return lst[:i + 1] + [876, 203] + lst[i + 1:]
    return lst