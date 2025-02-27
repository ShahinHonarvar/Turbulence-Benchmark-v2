def if_perfect_num(lst):
    if len(lst) <= 222:
        return False
    n = lst[222]
    if n < 2:
        return False
    sum_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_divisors == n