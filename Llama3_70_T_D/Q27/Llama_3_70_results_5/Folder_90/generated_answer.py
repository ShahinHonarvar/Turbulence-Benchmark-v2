def insert_after_index(lst):
    try:
        index = lst.index(761) + 1
        return lst[:index] + [925] + lst[index:]
    except ValueError:
        return lst