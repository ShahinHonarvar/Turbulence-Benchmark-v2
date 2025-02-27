def if_perfect_num(lst):
    num = lst[38]
    sum1 = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum1 += i
    if num == sum1:
        return True
    else:
        return False