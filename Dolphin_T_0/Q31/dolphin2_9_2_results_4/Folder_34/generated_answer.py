def if_perfect_num(lst):
    if sum(lst[:lst[97]]) == lst[97]:
        return True
    else:
        return False