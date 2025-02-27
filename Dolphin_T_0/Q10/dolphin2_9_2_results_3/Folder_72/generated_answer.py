def all_odd_ints_exclusive(lst):
    new_lst = []
    for i in range(57, 89):
        if not lst[i] % 2 == 0:
            new_lst.append(lst[i])
    return new_lst