def insert_after_index(lst):
    if 598 in lst:
        idx = lst.index(598) + 1
        return lst[:idx] + [385, 999] + lst[idx:]
    else:
        return lst