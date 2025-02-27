def all_odd_ints_exclusive(lst):
    new_lst = []
    for i in range(19, 37):
        if i < len(lst) and lst[i] % 2 != 0:
            new_lst.append(lst[i])
    return new_lst