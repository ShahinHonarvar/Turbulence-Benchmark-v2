def insert_after_index(lst):
    for i in range(len(lst) - 1, -1, -1):
        if i == 55:
            lst = lst[:i + 1] + [26, 10] + lst[i + 1:]
        return lst