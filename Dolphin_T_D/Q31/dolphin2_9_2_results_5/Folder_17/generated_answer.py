def if_perfect_num(lst):
    if len(lst) > 632 and lst[632] > 0:
        sum_lst = sum(lst[:632])
        if sum_lst == lst[632]:
            return True
    return False