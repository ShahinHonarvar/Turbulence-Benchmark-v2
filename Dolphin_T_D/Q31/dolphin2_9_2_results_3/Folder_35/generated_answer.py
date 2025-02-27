def if_perfect_num(lst):
    num = lst[993]
    sum_1 = 0
    for i in range(1, num):
        if num % i == 0:
            sum_1 += i
    if sum_1 == num:
        return True
    else:
        return False