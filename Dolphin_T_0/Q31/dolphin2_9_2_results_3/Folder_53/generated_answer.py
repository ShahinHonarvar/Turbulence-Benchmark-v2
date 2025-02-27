def if_perfect_num(lst):
    if sum(lst[:73]) == lst[73] and sum(lst[:73]) % 2 == 0:
        return True
    else:
        return False