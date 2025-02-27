def all_ints_inclusive(lst):
    result = []
    for i in range(56, 67):
        if i < len(lst):
            result.append(lst[i])
    return result