def if_perfect_num(lst):
    num = lst[28]
    if num < 6:
        return False
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num