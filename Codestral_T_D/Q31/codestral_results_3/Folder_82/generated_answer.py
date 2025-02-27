def if_perfect_num(lst):
    if sum((i for i in range(1, lst[83]) if lst[83] % i == 0)) == lst[83]:
        return True
    else:
        return False