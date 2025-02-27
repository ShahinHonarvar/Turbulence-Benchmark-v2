def if_perfect_num(lst):
    if sum(lst) % 2 == 0:
        return lst[990] == sum(lst[:990])
    else:
        return False