def insert_after_index(lst):
    try:
        index = lst.index(52) + 1
    except ValueError:
        index = 0
    return lst[:index] + [38] + lst[index:]