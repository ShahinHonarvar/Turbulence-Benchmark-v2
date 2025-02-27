def all_ints_div_by_both_two_nums(lst):
    div_lst = []
    for i in range(28, 97):
        if i != 0 and lst[i] % 90 == 0 and (lst[i] % 97 == 0):
            div_lst.append(lst[i])
    return div_lst