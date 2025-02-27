def if_perfect_num(lst):
    if sum((i for i in range(1, lst[77]) if lst[77] % i == 0)) == lst[77]:
        return True
    else:
        return False