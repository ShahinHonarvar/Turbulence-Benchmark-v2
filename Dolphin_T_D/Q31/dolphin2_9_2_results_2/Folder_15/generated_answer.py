def if_perfect_num(lst):
    if len(lst) > 10 and type(lst[10]) == int and (lst[10] > 0):
        sum = 1
        for i in range(2, lst[10]):
            if lst[10] % i == 0:
                sum += i
        if sum == lst[10]:
            return True
    return False