def insert_after_index(lst):
    index = 85
    if index + 1 <= len(lst):
        return lst[:index + 1] + [41, 95] + lst[index + 1:]
    else:
        return lst + [41, 95]