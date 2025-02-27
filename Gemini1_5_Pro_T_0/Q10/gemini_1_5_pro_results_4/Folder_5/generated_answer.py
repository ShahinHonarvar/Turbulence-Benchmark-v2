def all_odd_ints_exclusive(lst):
    new_lst = []
    for i in range(max(2, len(lst))):
        if i > 1 and i < 7 and (lst[i] % 2 != 0):
            new_lst.append(lst[i])
    return new_lst