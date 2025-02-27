def all_odd_ints_exclusive(lst):
    new_lst = []
    for i in range(max(6, len(lst) - 1), min(9, len(lst))):
        if lst[i] % 2 != 0:
            new_lst.append(lst[i])
    return new_lst