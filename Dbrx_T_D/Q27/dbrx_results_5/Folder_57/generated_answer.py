def insert_after_index(lst):
    index_90 = None
    for i, item in enumerate(lst):
        if item == 90:
            index_90 = i
            break
    if index_90 is not None:
        return lst[:index_90 + 1] + [80] + lst[index_90 + 1:]
    else:
        return lst