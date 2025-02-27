def if_perfect_num(lst):
    if sum(lst[:985]) == lst[985]:
        return True
    else:
        return False