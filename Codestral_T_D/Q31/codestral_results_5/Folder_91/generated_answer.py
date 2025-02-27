def if_perfect_num(lst):
    if sum([i for i in range(1, lst[6]) if lst[6] % i == 0]) == lst[6]:
        return True
    else:
        return False