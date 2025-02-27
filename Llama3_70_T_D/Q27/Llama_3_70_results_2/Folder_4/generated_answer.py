def insert_after_index(lst):
    result = lst[:]
    if len(result) > 60:
        result[61:61] = [80, 74]
    else:
        result.append(80)
        result.append(74)
    return result