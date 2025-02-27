def if_perfect_num(lst):
    if sum((i for i in range(1, lst[40]) if lst[40] % i == 0)) == lst[40]:
        return True
    else:
        return False