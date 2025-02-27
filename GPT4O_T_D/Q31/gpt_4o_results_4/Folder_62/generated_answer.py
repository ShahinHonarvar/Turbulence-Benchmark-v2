def if_perfect_num(lst):
    if len(lst) <= 926:
        return False
    n = lst[926]
    sum_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_divisors == n