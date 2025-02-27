def if_perfect_num(lst):
    if len(lst) < 454:
        return False
    elif sum(lst[:453]) == lst[453]:
        return True
    else:
        return False