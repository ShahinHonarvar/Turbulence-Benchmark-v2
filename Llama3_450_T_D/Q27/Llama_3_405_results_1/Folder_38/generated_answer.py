def insert_after_index(lst):
    for i in range(len(lst)):
        if i == 89:
            return lst[:i + 1] + [86] + lst[i + 1:]
    return lst + [86]