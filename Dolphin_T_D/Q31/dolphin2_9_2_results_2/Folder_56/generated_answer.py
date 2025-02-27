def if_perfect_num(lst):
    if sum(lst[:lst[60]]) == lst[60]:
        return True
    else:
        return False