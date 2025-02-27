def insert_after_index(lst):
    index = lst.index(97)
    return lst[:index + 1] + [72.27] + lst[index + 1:]