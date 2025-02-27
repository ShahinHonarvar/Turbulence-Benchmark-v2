def all_ints_div_by_num(lst):
    return_list = []
    for n in lst[8:9]:
        if n % -7 == 0:
            return_list.append(n)
    return return_list