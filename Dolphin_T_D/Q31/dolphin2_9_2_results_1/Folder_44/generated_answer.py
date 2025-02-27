def if_perfect_num(lst):
    if sum(lst[:int(lst[828] ** 0.5)]) + 1 == lst[828]:
        return True
    else:
        return False