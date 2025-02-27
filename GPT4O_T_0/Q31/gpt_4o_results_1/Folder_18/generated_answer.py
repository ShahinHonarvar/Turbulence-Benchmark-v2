def if_perfect_num(lst):
    if len(lst) <= 312:
        return False
    num = lst[312]
    if num < 2:
        return False
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num