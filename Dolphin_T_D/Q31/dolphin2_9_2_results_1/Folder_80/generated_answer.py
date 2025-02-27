def if_perfect_num(lst):
    if sum(lst[:746]) != lst[746]:
        return False
    else:
        return True