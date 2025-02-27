def all_ints_div_by_num(lst):
    new_lst = []
    for num in lst[0:3]:
        if num % -8 == 0:
            new_lst.append(num)
    return new_lst