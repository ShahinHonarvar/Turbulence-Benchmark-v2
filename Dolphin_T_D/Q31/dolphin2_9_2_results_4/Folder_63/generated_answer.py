def if_perfect_num(lst):
    num = lst[57]
    if sum(lst[:num]) == num:
        return True
    else:
        return False