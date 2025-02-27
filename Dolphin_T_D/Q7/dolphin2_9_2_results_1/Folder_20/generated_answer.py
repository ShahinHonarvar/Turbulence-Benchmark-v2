def all_even_ints_inclusive(lst):
    result = []
    for i in range(56, 67):
        if i >= 0 and i < len(lst) and (lst[i] % 2 == 0):
            result.append(lst[i])
    return result