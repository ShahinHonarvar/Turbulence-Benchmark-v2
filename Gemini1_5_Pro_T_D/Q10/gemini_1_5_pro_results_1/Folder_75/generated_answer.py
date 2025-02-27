def all_odd_ints_exclusive(lst):
    new_lst = []
    for i in range(21, 36):
        if i % 2 != 0 and i < len(lst):
            new_lst.append(lst[i])
    return new_lst