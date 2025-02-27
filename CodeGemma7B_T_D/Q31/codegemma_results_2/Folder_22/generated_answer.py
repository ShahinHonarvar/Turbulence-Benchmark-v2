def if_perfect_num(lst):
    if lst[72] % sum(range(1, lst[72])) == 0:
        return True
    else:
        return False