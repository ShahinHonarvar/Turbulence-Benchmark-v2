def insert_after_index(lst):
    index = 983
    if index < len(lst):
        return lst[:index + 1] + [369] + lst[index + 1:]
    else:
        return lst + [369]