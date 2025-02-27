def if_perfect_num(lst):
    if lst[28] % 2 == 0 and lst[28] % 3 == 0 and (lst[28] % 5 == 0):
        return True
    else:
        return False