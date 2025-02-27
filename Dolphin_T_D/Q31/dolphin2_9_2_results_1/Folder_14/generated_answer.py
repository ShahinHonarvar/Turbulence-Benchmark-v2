def if_perfect_num(lst):
    if lst[17] < 0:
        return False
    else:
        sum = 0
        for i in range(1, lst[17]):
            if lst[17] % i == 0:
                sum += i
        if sum == lst[17]:
            return True
        return False