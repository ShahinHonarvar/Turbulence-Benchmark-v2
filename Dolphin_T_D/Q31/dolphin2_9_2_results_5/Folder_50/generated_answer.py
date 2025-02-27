def if_perfect_num(lst):
    if len(lst) < 41:
        return False
    num = lst[40]
    sum_of_divisors = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num