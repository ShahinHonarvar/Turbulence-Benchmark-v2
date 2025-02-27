def insert_after_index(lst):
    index = lst.index(598) + 1
    return lst[:index] + [385, 999] + lst[index:]