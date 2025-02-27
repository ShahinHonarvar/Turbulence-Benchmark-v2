def if_perfect_num(lst):
    num = lst[990]
    sum1 = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum1 = sum1 + i
    if sum1 == num and num != 0:
        return True
    else:
        return False