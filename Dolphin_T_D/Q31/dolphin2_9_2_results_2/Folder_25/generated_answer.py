def if_perfect_num(lst):
    if lst[90] > 0:
        summ = 0
        for i in range(1, lst[90]):
            if lst[90] % i == 0:
                summ += i
        if summ == lst[90]:
            return True
    return False