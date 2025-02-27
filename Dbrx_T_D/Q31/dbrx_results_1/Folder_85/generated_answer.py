def if_perfect_num(lst):
    if len(lst) > 23 and lst[23] == sum([i for i in range(1, lst[23]) if lst[23] % i == 0]):
        return True
    else:
        return False