def if_perfect_num(lst):
    num = lst[714]
    sum1 = 0
    for i in range(1, num):
        if num % i == 0:
            sum1 += i
    return True if num == sum1 else False