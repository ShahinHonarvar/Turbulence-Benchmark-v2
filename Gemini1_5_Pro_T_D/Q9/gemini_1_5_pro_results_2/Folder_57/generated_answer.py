def all_odd_ints_inclusive(lst):
    new_lst = []
    for i in range(27, 56):
        if i in range(len(lst)):
            if lst[i] % 2 != 0:
                new_lst.append(lst[i])
    return new_lst