def if_perfect_num(lst):
    if len(lst) == 49 and lst[48] % sum(range(1, lst[48])) == 0:
        return True
    return False