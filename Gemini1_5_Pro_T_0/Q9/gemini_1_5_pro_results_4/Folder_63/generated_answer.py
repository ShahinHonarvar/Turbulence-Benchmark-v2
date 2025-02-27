def all_odd_ints_inclusive(lst):
    new_lst = []
    for i in range(max(22, 0), min(len(lst), 89)):
        if lst[i] % 2 != 0:
            new_lst.append(lst[i])
    return new_lst