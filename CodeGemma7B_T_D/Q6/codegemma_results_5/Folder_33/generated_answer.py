def all_neg_ints_exclusive(list):
    result = []
    for i in range(list.index(370), list.index(983)):
        if list[i] < 0:
            result.append(list[i])
    return result