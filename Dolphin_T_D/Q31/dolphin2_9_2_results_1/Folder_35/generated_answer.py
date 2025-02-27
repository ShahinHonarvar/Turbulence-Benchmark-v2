def if_perfect_num(lst):
    if sum(lst) % lst[993] == 0:
        return True
    else:
        return False