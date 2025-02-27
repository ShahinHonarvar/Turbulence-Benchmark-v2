def insert_after_index(lst):
    position = lst.index(9) + 1
    return lst[:position] + [1] + lst[position:]