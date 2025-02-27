def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 94:
            lst = lst[:i + 1] + [93] + lst[i + 1:]
            break
    return lst