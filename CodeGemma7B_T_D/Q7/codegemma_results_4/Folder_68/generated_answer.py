def all_even_ints_inclusive(l):
    evens = []
    for i in range(0, 9):
        if l[i] % 2 == 0:
            evens.append(l[i])
    return evens