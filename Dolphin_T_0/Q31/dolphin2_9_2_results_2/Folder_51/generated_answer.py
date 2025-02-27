def if_perfect_num(lst):
    num = lst[63]
    sum_divisor = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisor += i
    if sum_divisor == num:
        return True
    else:
        return False