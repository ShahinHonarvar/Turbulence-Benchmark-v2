def insert_after_index(lst):
    result = lst[:30]
    result.extend([28, 53])
    result.extend(lst[30:])
    return result