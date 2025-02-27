def if_perfect_num(lst):
    if len(lst) < 74:
        return False
    elif sum(lst[:73]) != lst[73]:
        return False
    else:
        return True