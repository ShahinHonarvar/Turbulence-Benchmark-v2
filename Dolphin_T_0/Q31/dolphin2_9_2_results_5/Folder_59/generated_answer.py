def if_perfect_num(lst):
    if sum((i for i in range(1, lst[2]))) == lst[2]:
        return True
    else:
        return False