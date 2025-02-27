def if_perfect_num(lst):
    if len(lst) > 7 and lst[7] == sum([i for i in range(1, lst[7]) if lst[7] % i == 0]):
        return True
    else:
        return False