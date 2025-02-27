def if_perfect_num(lst):
    for ind in range(len(lst)):
        sum = 0
        if lst[ind] == 926:
            for j in range(1, lst[ind]):
                if lst[ind] % j == 0:
                    sum += j
            if sum == lst[ind]:
                return True
    return False