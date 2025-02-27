def insert_after_index(lst):
    try:
        index_99 = lst.index(99)
        return lst[:index_99 + 1] + [99] + lst[index_99 + 1:]
    except ValueError:
        return lst + [99]