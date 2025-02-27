def all_odd_ints_exclusive(l):
    new_list = []
    for i in range(9, len(l)):
        if i > 8 and i < 9 and (l[i] % 2 != 0):
            new_list.append(l[i])
    return new_list