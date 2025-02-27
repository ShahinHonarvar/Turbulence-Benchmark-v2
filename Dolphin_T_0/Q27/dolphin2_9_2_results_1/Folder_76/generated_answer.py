def insert_after_index(lst):
    if 166 in lst:
        index = lst.index(166)
        return lst[:index + 1] + [232] + lst[index + 1:]
    else:
        return lst + [232]