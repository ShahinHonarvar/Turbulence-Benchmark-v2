def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 56 and i + 1 < len(lst) and (lst[i + 1] != 54):
            return lst[:i + 1] + [54] + lst[i + 1:]
    return lst + [54]