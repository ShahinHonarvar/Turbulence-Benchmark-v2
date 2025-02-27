def if_perfect_num(lst):
    if len(lst) <= 162:
        return False
    n = lst[162]
    if n < 2:
        return False
    divisors_sum = sum((i for i in range(1, n) if n % i == 0))
    return divisors_sum == n