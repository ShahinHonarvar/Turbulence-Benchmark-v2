def all_ints_div_by_both_two_nums(lst):
    new_lst = []
    for i in lst[8:10]:
        if i % 6 == 0 and i % 3 == 0:
            new_lst.append(i)
    if not new_lst:
        return []
    return new_lst