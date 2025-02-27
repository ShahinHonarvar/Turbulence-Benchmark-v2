def all_odd_ints_exclusive(lst):
    new_lst = []
    for i in range(101, 102):
        if i >= len(lst) or i < 0:
            return new_lst
        if lst[i] % 2 != 0:
            new_lst.append(lst[i])
    return new_lst