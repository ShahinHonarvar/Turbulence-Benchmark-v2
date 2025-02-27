def if_perfect_num(lst):
    if sum(lst[:410]) == lst[410]:
        return True
    else:
        return False