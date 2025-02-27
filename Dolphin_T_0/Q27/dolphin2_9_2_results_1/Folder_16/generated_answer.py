def insert_after_index(lst):
    position = lst.index(983)
    return lst[:position + 1] + [369] + lst[position + 1:]