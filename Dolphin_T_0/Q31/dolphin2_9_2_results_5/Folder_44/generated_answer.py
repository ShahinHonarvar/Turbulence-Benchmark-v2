def if_perfect_num(lst):
    if sum(lst[:828]) == lst[828]:
        return True
    else:
        return False