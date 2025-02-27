def if_perfect_num(lst):
    if len(lst) <= 537:
        return False
    num = lst[537]
    if num < 2:
        return False
    sum_of_divisors = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num