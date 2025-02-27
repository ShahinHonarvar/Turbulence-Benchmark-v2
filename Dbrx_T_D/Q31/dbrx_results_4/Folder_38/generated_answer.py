def if_perfect_num(lst):
    if len(lst) > 38 and lst[38] == sum([i for i in range(1, lst[38]) if lst[38] % i == 0]):
        return True
    else:
        return False