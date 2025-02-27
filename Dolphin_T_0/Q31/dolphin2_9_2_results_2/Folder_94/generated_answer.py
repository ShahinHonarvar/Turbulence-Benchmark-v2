def if_perfect_num(lst):
    if sum(lst) % lst[93] == 0 and lst[93] != 0:
        return True
    else:
        return False