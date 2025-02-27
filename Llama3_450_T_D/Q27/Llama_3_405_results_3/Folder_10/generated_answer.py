def insert_after_index(lst):
    try:
        index = lst.index(56) + 1
    except ValueError:
        index = len(lst)
    return lst[:index] + [54] + lst[index:]