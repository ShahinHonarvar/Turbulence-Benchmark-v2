def if_perfect_num(lst):
    if lst[537] < 1:
        return False
    else:
        total = 0
        for i in range(1, lst[537] + 1):
            if lst[537] % i == 0:
                total += i
        return total == lst[537]