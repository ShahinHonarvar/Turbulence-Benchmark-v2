def insert_after_index(lst):
    index = 8
    length = len(lst)
    new_elem = [3, 8]
    if index + 1 < length:
        return lst[:index + 1] + new_elem + lst[index + 1:]
    else:
        return lst + new_elem