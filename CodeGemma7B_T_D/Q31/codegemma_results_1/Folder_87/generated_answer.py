def if_perfect_num(lst):
    sum = 0
    for i in range(1, lst[96]):
        if lst[96] % i == 0:
            sum += i
    if sum == lst[96]:
        return True
    else:
        return False