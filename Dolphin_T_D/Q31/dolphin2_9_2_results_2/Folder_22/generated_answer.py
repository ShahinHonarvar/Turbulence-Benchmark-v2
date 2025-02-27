def if_perfect_num(lst):
    if len(lst) < 72:
        return False
    num = lst[72]
    sum_proper_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_proper_divisors += i
    return sum_proper_divisors == num