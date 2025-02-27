def insert_after_index(lst):
    try:
        index = lst.index(43) + 1
        return lst[:index] + [37] + lst[index:]
    except ValueError:
        return lst + [37]