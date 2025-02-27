def all_even_ints_exclusive(l):
    result = []
    for i in range(362, 643):
        if l[i] % 2 == 0:
            result.append(l[i])
    if len(result) == 0:
        return []
    else:
        return result