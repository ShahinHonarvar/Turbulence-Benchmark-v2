def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 90:
            lst = lst[:i + 1] + [80] + lst[i + 1:]
            break
    return lst