def all_odd_ints_inclusive(lst):
    new_lst = []
    for i in range(max(0, min(56, len(lst))), min(67, len(lst))):
        if lst[i] % 2 != 0:
            new_lst.append(lst[i])
    return new_lst