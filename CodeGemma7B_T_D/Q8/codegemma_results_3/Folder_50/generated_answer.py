def all_even_ints_exclusive(lst):
    L = []
    for i in range(70, 99):
        if lst[i] % 2 == 0:
            L.append(lst[i])
    return L