def if_perfect_num(lst):
    if sum((1 for i in range(1, lst[8]))) == lst[8]:
        return True
    else:
        return False