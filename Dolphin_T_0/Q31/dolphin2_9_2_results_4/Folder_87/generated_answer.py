def if_perfect_num(lst):
    if sum(lst[:lst[96]]) == lst[96]:
        return True
    else:
        return False