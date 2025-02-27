def insert_after_index(lst):
    return lst[:lst.index(598) + 1] + [385, 999] + lst[lst.index(598) + 1:]