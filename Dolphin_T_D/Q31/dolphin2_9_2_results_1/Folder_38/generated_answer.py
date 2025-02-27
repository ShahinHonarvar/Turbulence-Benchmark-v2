def if_perfect_num(lst):
    if len(lst) < 39:
        return False
    num = lst[38]
    sum1 = 0
    for i in range(1, num):
        if num % i == 0:
            sum1 += i
    return sum1 == num