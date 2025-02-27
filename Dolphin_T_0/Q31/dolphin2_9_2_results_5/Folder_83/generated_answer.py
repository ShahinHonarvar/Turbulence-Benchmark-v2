def if_perfect_num(lst):
    if sum(lst[:lst[95]]) == lst[95] and lst[95] != 0:
        return True
    else:
        return False