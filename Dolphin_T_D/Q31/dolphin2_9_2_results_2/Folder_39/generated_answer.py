def if_perfect_num(lst):
    if sum(lst[:lst[59]]) == lst[59] and lst[59] != 0:
        return True
    else:
        return False