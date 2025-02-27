def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 99:
            return lst[:i + 1] + [15] + lst[i + 1:]
    return lst + [15]