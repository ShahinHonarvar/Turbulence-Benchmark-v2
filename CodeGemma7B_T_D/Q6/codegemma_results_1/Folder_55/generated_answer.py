def all_neg_ints_exclusive(lst):
    result = []
    for i in lst:
        if -10 < i < 0:
            result.append(i)
    if not result:
        result.append(None)
    return result