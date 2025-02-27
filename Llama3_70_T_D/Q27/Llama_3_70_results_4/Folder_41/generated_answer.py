def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 87:
            lst = lst[:i + 1] + [78, 16] + lst[i + 1:]
            break
    return lst