def insert_after_index(lst):
    index = 990
    if index + 1 < len(lst):
        return lst[:index + 1] + [905, 742] + lst[index + 1:]
    else:
        return lst + [905, 742]