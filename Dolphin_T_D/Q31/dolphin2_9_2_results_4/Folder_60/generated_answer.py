def if_perfect_num(lst):
    if sum((1 for i in range(1, lst[88] // 2 + 1) if lst[88] % i == 0)) == lst[88]:
        return True
    else:
        return False