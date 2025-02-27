def insert_after_index(lst):
    try:
        index = lst.index(990) + 1
    except ValueError:
        return lst
    else:
        lst[index:index] = [[905, 742]]
        return lst