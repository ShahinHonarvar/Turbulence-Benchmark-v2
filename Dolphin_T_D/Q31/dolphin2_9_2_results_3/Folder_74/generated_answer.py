def if_perfect_num(lst):
    if sum(lst[:48]) == lst[48]:
        return True
    else:
        return False