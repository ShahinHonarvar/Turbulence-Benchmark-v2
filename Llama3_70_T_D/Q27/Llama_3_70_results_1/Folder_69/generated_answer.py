def insert_after_index(lst):
    index = 564
    if index < len(lst):
        return lst[:index + 1] + [149] + lst[index + 1:]
    else:
        return lst + [149]