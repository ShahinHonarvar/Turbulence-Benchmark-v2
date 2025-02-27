def all_odd_ints_inclusive(lst):
    new_lst = []
    for i in range(70, 85):
        if i < len(lst) and lst[i] % 2 != 0:
            new_lst.append(lst[i])
    return new_lst