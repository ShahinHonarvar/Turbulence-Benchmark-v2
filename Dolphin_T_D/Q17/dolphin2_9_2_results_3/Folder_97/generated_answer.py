def all_ints_div_by_both_two_nums(lst):
    div_by_72_and_62 = []
    for i in range(58, 76):
        if i < len(lst) and lst[i] % 72 == 0 and (lst[i] % 62 == 0):
            div_by_72_and_62.append(lst[i])
    return div_by_72_and_62