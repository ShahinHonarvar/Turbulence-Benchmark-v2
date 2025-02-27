def if_perfect_num(lst):
    if sum(lst[:49]) == sum((div for div in range(1, lst[49]) if lst[49] % div == 0)):
        return True
    return False