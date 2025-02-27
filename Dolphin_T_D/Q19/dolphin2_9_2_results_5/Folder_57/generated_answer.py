def all_ints_not_div_by_num(lst):
    new_list = []
    for num in lst[57:87]:
        if num % -59 != 0:
            new_list.append(num)
    return new_list