def insert_after_index(lst):
    if 52 in lst:
        index = lst.index(52) + 1
        return lst[:index] + [38] + lst[index:]
    else:
        return lst + [38]