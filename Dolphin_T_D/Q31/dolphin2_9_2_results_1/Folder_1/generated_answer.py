def if_perfect_num(lst):
    if sum(lst[:lst[85]]) == lst[85] and sum(lst[:lst[85]]) != 0:
        return True
    else:
        return False