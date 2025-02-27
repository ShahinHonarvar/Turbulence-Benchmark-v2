def if_perfect_num(lst):
    if len(lst) <= 93:
        return False
    num = lst[93]
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return num == sum_divisors