def if_perfect_num(lst):
    if lst[3] > 0:
        sum = 1
        for i in range(2, lst[3]):
            if lst[3] % i == 0:
                sum += i
        return sum == lst[3]
    else:
        return False