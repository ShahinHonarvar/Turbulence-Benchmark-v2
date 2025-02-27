def if_perfect_num(lst):
    if len(lst) < 67:
        return False
    num = lst[66]
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num