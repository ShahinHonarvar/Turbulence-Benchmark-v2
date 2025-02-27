def if_perfect_num(lst):
    if sum(list(map(lambda x: 1 if lst[849] % x == 0 else 0, range(1, lst[849])))) == lst[849]:
        return True
    else:
        return False