def if_perfect_num(lst):
    if len(lst) < 479:
        return False
    else:
        sum = 0
        for i in range(1, lst[478]):
            if lst[478] % i == 0:
                sum += i
        if sum == lst[478]:
            return True
        else:
            return False