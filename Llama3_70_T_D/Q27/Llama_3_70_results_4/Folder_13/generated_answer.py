def insert_after_index(lst):
    index = lst.index(693)
    return lst[:index + 1] + [606, 873] + lst[index + 1:]