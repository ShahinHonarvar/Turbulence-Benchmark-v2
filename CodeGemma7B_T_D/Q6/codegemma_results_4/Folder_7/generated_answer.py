def all_neg_ints_exclusive(list1):
    result = []
    for i in range(323, 972):
        if list1[i] < 0:
            result.append(list1[i])
    if len(result) == 0:
        return []
    else:
        return result