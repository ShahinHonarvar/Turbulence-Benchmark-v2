def if_perfect_num(lst):
    if len(lst) < 65:
        return False
    sum_div = 0
    num = lst[64]
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    return num == sum_div