def if_perfect_num(lst):
    if lst[247] % sum(range(2, int(lst[247] ** (1 / 2)) + 1)) == 0:
        return True
    else:
        return False