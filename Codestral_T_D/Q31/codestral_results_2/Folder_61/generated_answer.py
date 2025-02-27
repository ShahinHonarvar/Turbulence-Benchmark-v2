def if_perfect_num(lst):
    if sum([i for i in range(1, lst[8]) if lst[8] % i == 0]) == lst[8]:
        return True
    else:
        return False