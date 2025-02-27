def if_perfect_num(lst):
    if sum(lst[:849]) == lst[849]:
        return True
    else:
        return False