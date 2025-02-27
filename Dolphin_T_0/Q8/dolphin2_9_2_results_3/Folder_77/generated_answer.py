def all_even_ints_exclusive(lst):
    result = []
    for i in range(112, 473):
        if i % 2 == 0:
            result.append(lst[i])
    return result