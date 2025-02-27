def if_perfect_num(lst):
    if sum((i for i in range(1, lst[41]) if lst[41] % i == 0)) == lst[41]:
        return True
    return False