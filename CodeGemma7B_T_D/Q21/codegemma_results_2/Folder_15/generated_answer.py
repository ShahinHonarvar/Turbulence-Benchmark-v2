def all_ints_div_by_num(lst):
    new_lst = []
    for num in lst:
        if num % 3 == 0:
            new_lst.append(num)
    return new_lst