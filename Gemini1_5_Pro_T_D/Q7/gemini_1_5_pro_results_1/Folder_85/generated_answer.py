def all_even_ints_inclusive(l):
    new_list = []
    if len(l) < 9:
        return new_list
    for i in range(6, 9):
        if l[i] % 2 == 0:
            new_list.append(l[i])
    return new_list