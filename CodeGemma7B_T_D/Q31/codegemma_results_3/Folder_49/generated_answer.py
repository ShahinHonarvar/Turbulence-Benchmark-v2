def if_perfect_num(lst):
    summ = 0
    for i in range(1, lst[68]):
        if lst[68] % i == 0:
            summ += i
    if summ == lst[68]:
        return True
    else:
        return False