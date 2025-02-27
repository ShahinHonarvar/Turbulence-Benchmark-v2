def if_perfect_num(lst):
    num = lst[41]
    if sum(lst[:num]) == num:
        return True
    return False