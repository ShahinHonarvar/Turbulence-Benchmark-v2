def insert_after_index(lst):
    result = lst.copy()
    if len(result) > 1:
        if 693 in result:
            result.insert(result.index(693) + 1, [606, 873])
        else:
            result.append([606, 873])
    else:
        result.append([606, 873])
    return result