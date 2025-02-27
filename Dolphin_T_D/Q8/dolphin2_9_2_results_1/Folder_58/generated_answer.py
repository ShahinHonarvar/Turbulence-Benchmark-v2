def all_even_ints_exclusive(lst):
    result = []
    for i in range(276, 376):
        if i % 2 == 0:
            if i not in lst:
                result.append(i)
    return result