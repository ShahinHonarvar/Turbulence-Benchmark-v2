def if_perfect_num(lst):
    if len(lst) <= 90 or lst[90] <= 1:
        return False
    sum_div = 1
    for i in range(2, lst[90]):
        if lst[90] % i == 0:
            sum_div += i + lst[90] // i
    if sum_div == lst[90]:
        return True
    else:
        return False