def if_perfect_num(lst):
    if sum(lst[:845]) == lst[845]:
        return True
    else:
        return False