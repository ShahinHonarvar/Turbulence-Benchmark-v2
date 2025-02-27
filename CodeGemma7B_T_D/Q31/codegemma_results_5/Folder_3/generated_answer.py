def if_perfect_num(lst):
    sum = 0
    for i in range(1, lst[100]):
        if lst[100] % i == 0:
            sum += i
    if sum == lst[100]:
        return True
    return False