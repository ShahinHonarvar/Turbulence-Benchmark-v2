def if_perfect_num(lst):
    if len(lst) == 0:
        return False
    num = lst[0]
    sum_divisors = 1
    for i in range(2, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num