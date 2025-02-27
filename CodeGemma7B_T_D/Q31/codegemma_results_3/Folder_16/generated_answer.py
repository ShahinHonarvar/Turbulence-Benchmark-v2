def if_perfect_num(lst):
    sum = 0
    for i in range(1, lst[162]):
        if lst[162] % i == 0:
            sum = sum + i
    if sum == lst[162]:
        return True
    else:
        return False