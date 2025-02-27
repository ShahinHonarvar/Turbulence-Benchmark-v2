def if_perfect_num(lst):
    num = lst[126]
    if sum(lst[:num]) == num:
        return True
    else:
        return False