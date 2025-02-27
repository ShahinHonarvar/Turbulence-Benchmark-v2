def insert_after_index(lst):
    index = lst.index(70)
    return lst[:index + 1] + [185.43] + lst[index + 1:]