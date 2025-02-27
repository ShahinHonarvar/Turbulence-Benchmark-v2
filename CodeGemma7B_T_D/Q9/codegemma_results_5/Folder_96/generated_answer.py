def all_odd_ints_inclusive(L):
    for i in range(50, 201):
        if L[i] % 2 != 0:
            result.append(L[i])
    return result