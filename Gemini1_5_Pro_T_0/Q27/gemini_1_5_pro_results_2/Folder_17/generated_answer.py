def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 94:
            return lst[:i + 1] + [93] + lst[i + 1:]
    return lst