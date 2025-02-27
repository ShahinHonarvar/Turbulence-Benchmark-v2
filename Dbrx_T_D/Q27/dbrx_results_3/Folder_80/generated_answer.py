def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 95:
            return lst[:i + 1] + [43] + lst[i + 1:]
    return lst + [43]