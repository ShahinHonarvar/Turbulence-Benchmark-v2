def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 183:
            lst = lst[:i + 1] + [148, 145] + lst[i + 1:]
    return lst