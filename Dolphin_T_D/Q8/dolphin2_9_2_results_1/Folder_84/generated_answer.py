def all_even_ints_exclusive(ls):
    result = []
    for i in range(51, 92):
        if ls[i] % 2 == 0:
            result.append(ls[i])
    return result