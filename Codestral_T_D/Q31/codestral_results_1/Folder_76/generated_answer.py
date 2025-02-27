def if_perfect_num(lst):
    if sum((i for i in range(1, lst[537]) if lst[537] % i == 0)) == lst[537]:
        return True
    return False