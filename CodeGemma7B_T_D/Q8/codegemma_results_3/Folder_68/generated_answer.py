def all_even_ints_exclusive(listy):
    result = []
    for i in range(len(listy)):
        if listy[i] % 2 == 0 and i not in range(9):
            result.append(listy[i])
    return result