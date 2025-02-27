def all_odd_ints_inclusive(lst):
    new_lst = []
    if len(lst) > 85:
        for i in range(75, 86):
            if lst[i] % 2 != 0:
                new_lst.append(lst[i])
        return new_lst
    else:
        return []