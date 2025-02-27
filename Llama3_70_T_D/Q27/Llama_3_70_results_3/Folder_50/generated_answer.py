def insert_after_index(lst):
    index = lst.index(52)
    return lst[:index + 1] + [38] + lst[index + 1:]