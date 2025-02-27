def all_ints_div_by_num(lst):
    new_lst = []
    for i in lst[0:3]:
        if i % 3 == 0:
            new_lst.append(i)
    return new_lst