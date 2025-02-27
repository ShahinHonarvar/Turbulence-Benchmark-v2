def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == [87]:
            return lst[:i + 1] + [[78, 16]] + lst[i + 1:]
    return lst + [[78, 16]]