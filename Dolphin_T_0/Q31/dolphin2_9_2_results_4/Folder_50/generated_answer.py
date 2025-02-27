def if_perfect_num(lst):
    if len(lst) < 41:
        return False
    elif sum(lst[:40]) == lst[40]:
        return True
    else:
        return False