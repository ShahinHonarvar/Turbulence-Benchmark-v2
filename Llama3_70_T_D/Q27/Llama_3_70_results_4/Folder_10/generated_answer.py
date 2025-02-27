def insert_after_index(lst):
    return lst[:lst.index(56) + 1] + [54] + lst[lst.index(56) + 1:]