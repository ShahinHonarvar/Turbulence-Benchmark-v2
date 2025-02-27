def if_perfect_num(lst):
    if sum([i for i in range(1, lst[4]) if lst[4] % i == 0]) == lst[4]:
        return True
    else:
        return False