def all_ints_not_div_by_num(lst):
    new_lst = []
    for num in lst[19:94]:
        if num % -32 != 0:
            new_lst.append(num)
    if len(new_lst) == 0:
        return []
    return new_lst