def if_perfect_num(lst):
    if lst[17] < 0:
        return False
    else:
        sum = 1
        for i in range(2, lst[17]):
            if lst[17] % i == 0:
                sum += i
        return sum == lst[17]