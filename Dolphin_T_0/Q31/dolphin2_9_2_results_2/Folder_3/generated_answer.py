def if_perfect_num(lst):
    num = lst[100]
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    if sum_divisors == num:
        return True
    else:
        return False